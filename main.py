import os
import csv

from fm_index import FmIndex

fm = FmIndex("caca")

p = "a"

print(sorted(fm.occurrences(p)))


def main():
    user_input = 0
    while user_input != '1' and user_input != '2' and user_input != '3':
        print("Quels motifs chercher ? ")
        print("1 - Motifs aleatoires")
        print("2 - Motifs presents")
        print("3 - Tous motifs")
        print(user_input)
        print(type(user_input))
        user_input = input()
    

    texts_path = "data/split/"
    
    texts = [texts_path+"/"+f for f in os.listdir(texts_path) if os.path.isfile(os.path.join(texts_path, f))]

    hs = ["Longueur du Texte", "Temps de création de l'index"]
    data = []
    for text_filename in texts:
        with open(text_filename, "r", encoding="ISO-8859-1") as textfile:
            t = textfile.read()

            dir_name = text_filename[11:-4]

            patterns_path = f"data/patterns/{dir_name}/"
            user_choices = {
                "1": ["absent_patterns.txt"],
                "2": ["present_patterns.txt"],
                "3": ["absent_patterns.txt", "present_patterns.txt"]
            }


            print(f"Longueur du texte : {len(t)}")
            fm = FmIndex(t)
            for pattern_filename in user_choices[user_input]:
                with open(patterns_path+pattern_filename, "r", encoding="ISO-8859-1") as patternfile:
                    patterns = patternfile.readlines()

                    for pattern in patterns:
                        #print(sorted(fm.occurrences(pattern)))
                        fm.occurrences(pattern)

            data.append([len(t), fm.create_time])

    with open("results.csv", "w", encoding="utf8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(hs)
        writer.writerows(data)

    return 0

if __name__ == "__main__":
    main()