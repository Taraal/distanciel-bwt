import time
import os
from pattern_generator import generate_patterns
from text_generator import generate_texts


try:
    os.mkdir("data/split/")
except FileExistsError:
    pass

print("Génération des textes...")
generate_texts()
print("Done ! ")

time.sleep(2)

try:
    os.mkdir("data/patterns/")
except FileExistsError:
    pass

print("Génération des motifs...")
generate_patterns()
print("Done !" )
print("Préparation terminée")