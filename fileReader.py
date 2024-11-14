import os

INPUT_PATH = "input"
OUTPUT_PATH = "output"

#TODO right now just prints, eventually we will do more with files
def read_files(directory_path):
    for file in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file)
        with open(file_path, encoding="utf-8") as f:
            for line in f: 
                print(line.strip())

read_files(INPUT_PATH)
