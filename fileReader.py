import os
from languageProcessing import *
from tkinter import filedialog
import PyPDF2

INPUT_PATH = "input"
OUTPUT_PATH = "output"

def pdf_to_txt(pdf_file, txt_file):
    with open(pdf_file, 'rb') as pdf_reader:
        pdf = PyPDF2.PdfReader(pdf_reader)
        text = ""
        for page in pdf.pages:
            text += page.extract_text()

    with open(txt_file, 'w') as txt_writer:
        txt_writer.write(text)

def upload_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        src = file_path
        file_split = file_path.split('/')[-1].split(".")
        file_name = file_split[0]
        file_ext = file_split[1]
        dest = "./" + INPUT_PATH + "/" + file_name
        if file_ext == "pdf":
            pdf_to_txt(src, dest)
        else:
            command = "copy " + src + " " + dest
            os.system(command)

def download_files():
    downloads_dir = os.path.expanduser('~') + "\\" + "Downloads"
    output_dir = "\output"
    path = downloads_dir + output_dir
    #check if output already exists, if not then make it, if so create output(1), output(2)...
    if not os.path.exists(path):
        os.system("mkdir " + path)
    else:
        value = 0
        while os.path.exists(path):
            value += 1
            path = downloads_dir + output_dir + "(" + str(value) + ")"
        os.system("mkdir " + path)

    for file in os.listdir(OUTPUT_PATH):
        src = OUTPUT_PATH + "\\" + file
        command = "move " + src + " " + path + "\\"
        os.system(command)

def read_and_write_file(function, file):
    from languageProcessing import sentence_detection, word_frequency, named_entity_recognition
    file_path = os.path.join(INPUT_PATH, file)
    with open(file_path, encoding="utf-8") as f:
        output_text = ""
        text = f.read()
        if function == word_frequency:
            output_text = function(text)
        else:
            sentences = sentence_detection(text)
            for line in sentences: 
                output_text += function(line) + "\n"
        create_file(output_text, file)

def create_file(text, filename):
    with open(OUTPUT_PATH + "/" + filename, "w") as file:
        file.write(text)

def get_first_line(directory_path = INPUT_PATH):
    first_file = os.listdir(directory_path)[0]
    file_path = os.path.join(directory_path, first_file)
    with open(file_path, encoding="utf-8") as f:
        for line in f:
            return line