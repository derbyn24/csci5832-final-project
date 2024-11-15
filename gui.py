import tkinter as tk
import os
from tkinter import filedialog
from tkinter import ttk
from languageProcessing import *

def upload_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        #TODO copy the file to the input location
        print("Selected file:", file_path)

#TODO this current gui is a proof of concept and will be cleaned later
#Onclick: when a button is clicked, ex. lemmatization, it will only run on the first example
# sentence and change the mode to "lemmatization". 
# Then when "run" is clicked, it will run that paricular mode

def add_buttons():
    rightmost_col = 2

    pos_tagging_button = tk.Button(text="Part of Speech Tagging", command=part_of_speech_tagging)
    pos_tagging_button.grid(row=1, column=rightmost_col, padx=20, sticky="se")

    word_frequency_button = tk.Button(text="Word Frequency", command=word_frequency)
    word_frequency_button.grid(row=2, column=rightmost_col, padx=20, sticky="e")

    lemmatization_button = tk.Button(text="Lemmatization", command=lemmatization)
    lemmatization_button.grid(row=3, column=rightmost_col, padx=20, sticky="ne")

    chunking_button = tk.Button(text="Text Chunking", command=lemmatization)
    chunking_button.grid(row=4, column=rightmost_col, padx=20, sticky="ne")

    run_button = tk.Button(text="Run", command=lemmatization)
    run_button.grid(row=7, column=rightmost_col, pady=20, padx=20, sticky="e")

def add_example_boxes(): 
    input_box = tk.Label(text="Example Input", anchor="nw", bg="#c4c4c4", borderwidth=2, relief="groove")
    input_box.grid(row=0, column=0, rowspan=3, padx=10, pady=20, sticky="nswe")

    output_box = tk.Label(text="Output Preview", anchor="nw", bg="#e8e8e8", borderwidth=2, relief="groove")
    output_box.grid(row=3, column=0, rowspan=5, padx=10, pady=20, sticky="nswe")

def add_input_file():
    padding = 20
    upload_file_button = tk.Button(text="Upload File", command=upload_file)
    upload_file_button.grid(row=0, column=2, padx=padding, pady=padding, sticky="nswe")
    
    canvas = tk.Canvas(window, width=50, height=20)
    canvas.grid(row=0, column=1, padx=10, pady=20, sticky="nsew")

    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame)
    scrollbar = ttk.Scrollbar(window, orient="vertical", command=canvas.yview)
    scrollbar.grid(row=0, column=1, padx=10, pady=20, sticky="nse")
    canvas.configure(yscrollcommand=scrollbar.set)
    i = 0
    for file in os.listdir("input"):
        tk.Label(frame, text=file).grid(row=i, column=1)
        i += 1
    frame.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))

window = tk.Tk()
window.title("Natural Language Toolkit Visual Tool")
window.geometry("600x400")

window.grid_columnconfigure(0, weight=6)
window.grid_columnconfigure(1, weight=4)
window.grid_columnconfigure(2, weight=1)
window.grid_rowconfigure(0, weight=2)
window.grid_rowconfigure([1, 2, 3, 4, 5, 6, 7], weight=1)

add_input_file()
add_buttons()
add_example_boxes()

window.mainloop()