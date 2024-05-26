import os
import openai
import json
import sys
import tqdm
import time


def send_req(messages):
    """envoie une requête avec une liste de messages à chatpgt, et récupère le contenu de la réponse."""

    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0,
        max_tokens=None,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return "\n".join([i.message.content for i in response.choices])


def annotate_directory(chunks_dir):
    chunks_dir = os.path.realpath(chunks_dir)
    annotations_dir = chunks_dir.replace("/chunks/", "/annotations/")
    if not os.path.isdir(annotations_dir):
        os.mkdir(annotations_dir)

    def get_not_yet_annotated():
        chunk_files = set(os.listdir(chunks_dir))
        annotations_files = set(os.listdir(annotations_dir))
        files = chunk_files - annotations_files
        return files

    files = get_not_yet_annotated()

    total_n = len(files)
    n = 0
    x = 1

    while n < total_n and x < 10:
        print(f"reste à annoter {total_n - n} textes. essai numéro {x}/10")
        for fp in tqdm.tqdm(files):
            with open(os.path.join(chunks_dir, fp), "r") as f:
                messages = json.load(f)
            response = send_req(messages)
            try:
                r = json.loads(response)
                if r is not None:
                    with open(os.path.join(annotations_dir, fp), "w") as f:
                        json.dump(obj=r, fp=f, indent=1, ensure_ascii=False)
                    n += 1
            except json.decoder.JSONDecodeError:
                print("erreur de décodage: à corriger manuelement")
                with open(os.path.join(annotations_dir, fp + "_a_corriger"), "w") as f:
                    f.write(response)
                n += 1
        x += 1
        time.sleep(30)
        files = get_not_yet_annotated()


if __name__ == "__main__":
    chunk_dir = sys.argv[1]
    if os.path.isdir(chunk_dir):
        annotate_directory(chunk_dir)
        quit(0)
    else:
        raise ValueError("not a directory:", chunk_dir)
