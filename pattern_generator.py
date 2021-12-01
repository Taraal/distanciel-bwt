import os 
import random
import string

MIN_LENGTH = 4
MAX_LENGTH = 13 

NB_PRESENT_PATTERN = 80 
NB_ABSENT_PATTERN = 20 

split_path = "data/split/"
patterns_path = "data/patterns/"



files = [split_path+"/"+f for f in os.listdir(split_path) if os.path.isfile(os.path.join(split_path, f))]

def generate_patterns():
    for filename in files:
        dir_name = filename[11:-4]
        try:
            os.mkdir(patterns_path+"/"+dir_name)
        except FileExistsError:
            pass
        with open(filename, 'r', encoding="ISO-8859-1") as textfile:
            data = textfile.read().lower()
            
            with open(patterns_path+dir_name+"/present_patterns.txt", "w", encoding="ISO-8859-1") as pres_patternfile:
                for j in range(0, NB_PRESENT_PATTERN):
                    for i in range(MIN_LENGTH, MAX_LENGTH + 1):
                        starting_point = random.randint(0, len(data) - (MAX_LENGTH + 1))

                        pres_patternfile.write(data[starting_point:starting_point+i]+"\n")
            
            with open(patterns_path+dir_name+"/absent_patterns.txt", "w", encoding="ISO-8859-1") as abs_patternfile:
                for j in range(0, NB_ABSENT_PATTERN):
                    for i in range(MIN_LENGTH, MAX_LENGTH + 1):

                        chars = "".join([random.choice(string.ascii_letters) for k in range(i)] )
                        abs_patternfile.write(chars + "\n") # Need replacing with random words 


generate_patterns()