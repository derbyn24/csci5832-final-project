import tkinter as tk
import os
from tkinter import filedialog
from tkinter import ttk
from languageProcessing import *
from fileReader import *

mode_func = None
prev_button = None

#TODO this current gui is a proof of concept and will be cleaned later
#Onclick: when a button is clicked, ex. lemmatization, it will only run on the first example
# sentence and change the mode to "lemmatization". 
# Then when "run" is clicked, it will run that paricular mode on all files

def add_elements():
    rightmost_col = 2

    #input and output boxes
    input_text = tk.Label(text="Input:", anchor="n")
    input_text.grid(row=0, column=0, padx=10, sticky="nw")
    input_box = tk.Label(text="Input Preview...", fg="#2e2e2e", anchor="nw", bg="#c4c4c4", borderwidth=2, relief="groove")
    input_box.grid(row=0, column=0, rowspan=3, padx=10, pady=20, sticky="nswe")

    output_text = tk.Label(text="Sample Output:", anchor="n")
    output_text.grid(row=3, column=0, padx=10, sticky="nw")
    output_box = tk.Label(text="Output Preview...", fg="#2e2e2e", anchor="nw", bg="#e8e8e8", borderwidth=2, relief="groove")
    output_box.grid(row=3, column=0, rowspan=5, padx=10, pady=20, sticky="nswe")

    pos_tagging_button = tk.Button(text="Part of Speech Tagging", 
                                   command= lambda: change_mode(part_of_speech_tagging, pos_tagging_button, input_box, output_box))
    pos_tagging_button.grid(row=1, column=rightmost_col, padx=20, sticky="e")

    word_frequency_button = tk.Button(text="Word Frequency", 
                                      command=lambda: change_mode(word_frequency, word_frequency_button, input_box, output_box))
    word_frequency_button.grid(row=2, column=rightmost_col, padx=20, sticky="e")

    lemmatization_button = tk.Button(text="Lemmatization", 
                                     command=lambda: change_mode(lemmatization, lemmatization_button, input_box, output_box))
    lemmatization_button.grid(row=3, column=rightmost_col, padx=20, sticky="e")

    chunking_button = tk.Button(text="Text Chunking", 
                                command=lambda: change_mode(chunking, chunking_button, input_box, output_box))
    chunking_button.grid(row=4, column=rightmost_col, padx=20, sticky="e")

    run_button = tk.Button(text="Run", command=run_texts)
    run_button.grid(row=7, column=rightmost_col, pady=20, padx=20, sticky="e")

def add_input_file_upload():
    padding = 20
    upload_file_button = tk.Button(text="Upload File", command=upload_file)
    upload_file_button.grid(row=0, column=2, padx=padding, pady=padding, sticky="e")
    
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

def upload_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        #TODO copy the file to the input location
        print("Selected file:", file_path)

def create_gui(): 
    window.title("Natural Language Toolkit Visual Tool")
    window.geometry("600x400")
    window.grid_columnconfigure(0, weight=6)
    window.grid_columnconfigure(1, weight=4)
    window.grid_columnconfigure(2, weight=1)
    window.grid_rowconfigure(0, weight=2)
    window.grid_rowconfigure([1, 2, 3, 4, 5, 6, 7], weight=1)
    add_input_file_upload()
    add_elements()

def run_texts():
    #TODO this function will run all text with the selected mode
    pass

def change_mode(new_mode, button, input_box, output_box):
    global mode_func
    global prev_button
    if new_mode == mode_func:
        return
    button.config(relief="sunken")
    if prev_button is not None:
        prev_button.config(relief='raised')
    prev_button = button
    mode_func = new_mode
    original_sen, output_sen = run_first_sentence()
    change_text(original_sen, input_box, output_sen, output_box)

def run_first_sentence():
    line = get_first_line(INPUT_PATH)
    first_sentence = sentence_detection(line)[0]
    output_sentence = mode_func(first_sentence)
    return first_sentence, output_sentence

def change_text(input_text, input_box, output_text, output_box):
    input_box.config(text=input_text)
    output_box.config(text=output_text)

window = tk.Tk()

create_gui()

window.mainloop()