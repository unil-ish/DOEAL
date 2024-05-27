import json
import os
from clean_prepare_for_rdf import dict_iter_rec


class Lookup:

    """Assigne des IDS (utilisées pour les URIs) à chaque objets dans les fichiers JSONS.

    Chaque FictionalObject (FictionalCharacter, FictionalEvent, FictionalPlace) se voit attribué une ID qui se compose de son nom accolé au chemin de fichier de l'histoire dans lequel il se trouve et dans lequel il est, par conséquent, définit (par description).

    Par exemple:
        - texts/mobydick.txt#Captain_Ahab
        - texts/littlewomen.txt#Mother
        - texts/aroomwithaview.txt#Cecil_Vyse
    """

    def __init__(self):
        pass

    def new_story(self, story) -> None:
        if not isinstance(story, str):
            raise ValueError("`story` must be type `str`.")
        self.story = story
        self.table = {}
        self.curval = 0
        return

    def nextval(self) -> int:
        self.curval += 1
        return self.curval

    def generate_id(self, obj) -> str:
        # si l'objet a un nom, son ID dans la fiction est ce nom, sinon c'est simplement un nombre unique généré automatiquement.
        suffix = obj.get("name")
        if suffix is None:
            suffix = str(self.nextval())

        # tronquer si trop long
        if len(suffix) > 50:
            suffix = suffix[:50]

        # format: texts/mobydick#captain_ahab
        return f"texts/{self.story}.txt#{suffix}"

    def get_or_set_id(self, obj) -> None:
        name = obj["name"]
        getid = self.table.get(name)
        if getid is not None:
            _id = getid
        else:
            _id = self.generate_id(obj)
            self.table[name] = _id
        obj["id"] = _id
        return

    def add_all_ids(self, annote) -> None:
        def cond(obj):
            return "name" in obj.keys()

        dict_iter_rec(
            obj=annote,
            fn_condition=cond,
            fn_apply=self.get_or_set_id,
        )

        # seule exception: les emotions, qui ont un ID différent
        try:
            for character in annote["FictionalCharacters"]:
                for emotion in character["feels"]:
                    emotion["id"] = emotion["name"]
        except KeyError:
            pass
        except TypeError:
            pass
        return


if __name__ == "__main__":
    l = Lookup()

    root_directory = "../data/annotations_cleaned"
    for directory_name in os.listdir(root_directory):
        directory_path = os.path.join(root_directory, directory_name)
        l.new_story(directory_name)
        for filename in os.listdir(directory_path):
            fp = os.path.join(directory_path, filename)
            with open(fp, "r") as f:
                annote = json.load(f)
            l.add_all_ids(annote)
            with open(fp, "w") as f:
                json.dump(obj=annote, fp=f, indent=1, ensure_ascii=False)
