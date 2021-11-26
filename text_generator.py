import numpy as np 
import random


MIN_LENGTH = 13 # Nmin (13 étant la taille maximale d'un motif à rechercher, comme écrit sur le sujet du distanciel)
MAX_LENGTH = MIN_LENGTH * 201 # Nmax
NB_TXT = 10 # K (10 textes pour chaque fichier)
STEPS = np.linspace(MIN_LENGTH, MAX_LENGTH, num=NB_TXT) # Réparition des tailles de textes entre nmin et nmax


files = ['cancer_corpus_en.txt', 'cancer_corpus_fr.txt', 'europarl-corpus-en.txt', 'europarl-corpus-fr.txt']

def generate_texts():
    """
    Script de génération de K textes
    Objectif : A partir de 4 corpus, générer 40 textes (10 textes par corpus) de taille comprise entre nmin et nmax, nmax étant au moins 200 fois plus grand que nmin.
    """
    
    
    for file in files:
        with open('data/corpora/'+file, 'r', encoding="ISO-8859-1") as f: # Utf-8 gives a UnicodeDecodeError with accents in europarl corpora
            try:
                data = f.read()
            except UnicodeDecodeError as e:
                print(file)
                

            for index, step  in enumerate(STEPS):
                 # Pour chaque texte, on prend un emplacement aléatoire T dans le corpus 
                 # et on sectionne T + la taille N souhaitée du texte

                starting_point = random.randint(0, len(data))

                with open(f'data/split/{file[:-4]}-{index}.txt', 'w', encoding="ISO-8859-1") as fw:
                    fw.write(data[starting_point:starting_point+int(step)])
