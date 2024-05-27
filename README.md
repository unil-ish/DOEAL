# EMOTEL: "Emotion Ontology for Literary Exploration".

Une ontologie représentant les émotions dans des textes littéraires.

Ce projet a été réalisé dans le cadre du cours "Programmation pour le Web sémantique" de Davide Picca (SLI, Lettres, UNIL) au printemps 2024.

## But du projet

Ce projet cherche à représenter les émotions dans un texte littéraire en créant une ontologie à l'aide du logiciel [Protégé](https://protege.stanford.edu/).

Nous utilisons ensuite des LLMs (ici [ChatGPT](https://chatgpt.com/)) pour annoter nos textes puis des scripts python pour peupler notre ontologie.

## Étapes du projet

1. Identification des émotions et informations que nous souhaitons recenser dans notre ontologie. 

2. Alignement avec des ontologies existantes et récupération de classes et de propriétés intéressantes pour notre cas.

3. Création d'une hiérarchie de classe de notre ontologie.

4. Développement de prompts permettant d'extraire les informations nécessaires au peuplement de notre ontologie.

5. Développement de scripts permettant l'ajouts de nos individus dans l'ontologie.

## Structure de ce repository

| Dossier | Contenu |
|---------|---------|
| Data | Contient les données textuelles et JSON utilisées dans ce projet |
| Doc | Documentation concernant la construction de notre ontologie ainsi que de nos réflexions théoriques autour d'une ontologie des émotions littéraires |
| Ontology | Contient notre ontologie OWL de base créée avec [Protégé](https://protege.stanford.edu/) |
| Outputs | Contient l'ontologie peuplée par le script `json_to_owl.py`|
| Project guidelines | Contient le `README.md` officiel de la donnée du projet |
| Prompts | Contient différents itérations de la construction de nos prompts |
| Scripts | Contient les scripts conçus pour traiter nos données |

## Data

Ce dossier contient les éléments suivants:

- `annotations` : Contient les résultats de nos prompts appliqués aux textes de notre corpus et corrigés à certains endroits par nos soins
- `annotations_cleaned` : Contient les annotations corrigées par le script `normalize_names.py` qui sont ensuite utilisées pour peupler l'ontologie
- `chunks` : Contient les textes découpés pour être passés dans ChatGPT
- `texts` : Contient les fichiers textes originaux de notre corpus
- `textlist.md` : Contient la liste des textes de notre corpus

## Scripts

- `ask_chatgpt.py` : Annote les morceaux de textes envoyés à l'API CHatGPT
- `cut_text.py` : Coupe les fichiers textes après un certain nombre de caractères
- `json_to_owl.py` : Itère sur toutes les annotations de `annotations_cleaned` pour créer des individus et les njecter dans l'ontologie `ontology.owl`
- `normalize_names.py` : Sert à nettoyer les `annotations` pour enlever les espaces dans les noms par exemple



## Dépendances

Se référer au fichier requirements.txt pour une liste exacte.

Nous vous encourageons à exécuter nos scripts dans un environnement virtuel. Pour installer le fichier `requirements.txt`, exécutez la commande suivante dans un terminal:
- Unix/macOS: `python3 -m pip install -r requirements.txt`
- Windows: `py -m pip install -r requirements.txt`

## Crédits

Ce projet a été réalisé par: (TODO: corriger les noms)

- Zakari
- Amélie
- Annaël
- Thibault
- Johan

Développé à l'aide de la communauté Python et Protégé, ainsi qu'avec le soutien de ChatGPT.
