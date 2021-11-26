import os 
import random

MIN_LENGTH = 4
MAX_LENGTH = 13 

NB_PRESENT_PATTERN = 80 
NB_ABSENT_PATTERN = 20 

split_path = "data/split/"
patterns_path = "data/patterns/"

files = [split_path+"/"+f for f in os.listdir(split_path) if os.path.isfile(os.path.join(split_path, f))]

for filename in files:
    dir_name = filename[11:-4]
    try:
        os.mkdir(patterns_path+"/"+dir_name)
    except FileExistsError:
        pass
    with open(filename, 'r', encoding="ISO-8859-1") as textfile:
        data = textfile.read()
        for i in range(MIN_LENGTH, MAX_LENGTH):
            present_patterns = []
            with open(patterns_path+dir_name+"/present_patterns.txt", "w", encoding="ISO-8859-1") as pres_patternfile:
                for j in range(0, NB_PRESENT_PATTERN):
                    
                        
                    starting_point = random.randint(0, len(data))

                    pres_patternfile.write(data[starting_point:starting_point+i]+"\n")
            
            with open(patterns_path+dir_name+"/absent_patterns.txt", "w") as abs_patternfile:
                for j in range(0, NB_ABSENT_PATTERN):
                    starting_point = random.randint(0,len(data))
                    abs_patternfile.write(data[starting_point:starting_point+i] + "\n") # Need replacing with random words 




