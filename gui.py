import tkinter as tk
from tkinter import filedialog
from languageProcessing import *

def upload_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        #TODO copy the file to the input location
        print("Selected file:", file_path)

def add_buttons():
    upload_file_button = tk.Button(window, text="Upload File", command=upload_file)
    upload_file_button.pack(pady=20)
    pos_tagging_button = tk.Button(window, text="Part of Speech Tagging", command=part_of_speech_tagging)
    pos_tagging_button.pack(pady=20)
    word_frequency_button = tk.Button(window, text="Word Frequency", command=word_frequency)
    word_frequency_button.pack(pady=20)
    lemmatization_button = tk.Button(window, text="Lemmatization", command=lemmatization)
    lemmatization_button.pack(pady=20)

#TODO a lot of this will be cleaned up eventually
window = tk.Tk()
window.title("Natural Language Toolkit Visual Tool")
window.minsize(400, 400)
add_buttons()

window.mainloop()