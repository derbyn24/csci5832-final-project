import os
from languageProcessing import *
from tkinter import filedialog

INPUT_PATH = "input"
OUTPUT_PATH = "output"

def upload_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        src = file_path
        file_name = file_path.split('/')[-1].split(".")[0]
        dest = ".\\" + file_name
        command = "copy " + "\"" + src + "\" " + "\"" + dest + "\""
        # TODO Resolve errors
        os.system(command)

def read_and_write_files(function):
    for file in os.listdir(INPUT_PATH):
        file_path = os.path.join(INPUT_PATH, file)
        with open(file_path, encoding="utf-8") as f:
            output_text = ""
            for line in f: 
                for token in function(line):
                    output_text += "\n" + token
            create_file(output_text, file)

def create_file(text, filename):
    with open(OUTPUT_PATH + "/" + filename, "w") as file:
        file.write(text)

def get_first_line(directory_path):
    first_file = os.listdir(directory_path)[0]
    file_path = os.path.join(directory_path, first_file)
    with open(file_path, encoding="utf-8") as f:
        for line in f:
            return line