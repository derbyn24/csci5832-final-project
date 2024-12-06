import tkinter as tk
import os
from tkinter import ttk
from languageProcessing import *
from fileReader import *

mode_func = None
prev_button = None

def add_elements():
    rightmost_col = 2

    progress_bar = ttk.Progressbar(window, orient="horizontal", mode="determinate")
    progress_bar.grid(row=6, column=rightmost_col, padx=10, pady=10, sticky="nsew")
    progress_bar.grid_remove()

    run_button = tk.Button(text="Run", command=lambda: run_texts(run_button, progress_bar))
    run_button.grid(row=7, column=rightmost_col, pady=20, padx=20, sticky="e")
    run_button.config(state="disabled") #disable button until we select an option

    #input and output boxes
    input_text = tk.Label(text="Input:", anchor="n")
    input_text.grid(row=0, column=0, padx=10, sticky="nw")
    input_box = tk.Label(text="Input Preview...", fg="#2e2e2e", width=35, anchor="nw", bg="#c4c4c4", borderwidth=2, relief="groove", wraplength=250)
    input_box.grid(row=0, column=0, rowspan=3, padx=10, pady=20, sticky="nsw")

    output_text = tk.Label(text="Sample Output:", anchor="n")
    output_text.grid(row=3, column=0, padx=10, sticky="nw")
    output_box = tk.Label(text="Output Preview...", fg="#2e2e2e", width=35, anchor="nw", bg="#e8e8e8", borderwidth=2, relief="groove", wraplength=250)
    output_box.grid(row=3, column=0, rowspan=5, padx=10, pady=20, sticky="nsw")

    pos_tagging_button = tk.Button(text="Part of Speech Tagging", 
                                   command= lambda: change_mode(part_of_speech_tagging, pos_tagging_button, input_box, output_box, run_button))
    pos_tagging_button.grid(row=1, column=rightmost_col, padx=20, sticky="e")

    word_frequency_button = tk.Button(text="Word Frequency", 
                                      command=lambda: change_mode(word_frequency, word_frequency_button, input_box, output_box, run_button))
    word_frequency_button.grid(row=2, column=rightmost_col, padx=20, sticky="e")

    lemmatization_button = tk.Button(text="Lemmatization", 
                                     command=lambda: change_mode(lemmatization, lemmatization_button, input_box, output_box, run_button))
    lemmatization_button.grid(row=3, column=rightmost_col, padx=20, sticky="e")

    chunking_button = tk.Button(text="Text Chunking", 
                                command=lambda: change_mode(chunking, chunking_button, input_box, output_box, run_button))
    chunking_button.grid(row=4, column=rightmost_col, padx=20, sticky="e")

    download_file_button = tk.Button(text="Download Files", command=download_files)
    download_file_button.grid(row=7, column=rightmost_col - 1, padx=20, pady=20, sticky="e")

def add_input_file_upload():
    padding = 20
    
    canvas = tk.Canvas(window, width=50, height=20)
    canvas.grid(row=0, column=1, padx=10, pady=20, sticky="nsew")

    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame)
    scrollbar = ttk.Scrollbar(window, orient="vertical", command=canvas.yview)
    scrollbar.grid(row=0, column=1, padx=10, pady=20, sticky="nse")
    canvas.configure(yscrollcommand=scrollbar.set)
    i = 0
    for file in os.listdir(INPUT_PATH):
        tk.Label(frame, text=file).grid(row=i, column=1)
        i += 1
    frame.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))

    upload_file_button = tk.Button(text="Upload File", command=lambda: file_upload_request(frame))
    upload_file_button.grid(row=0, column=2, padx=padding, pady=padding, sticky="e")

def create_gui(): 
    window.title("Natural Language Toolkit Visual Tool")
    window.geometry("600x400")
    window.grid_columnconfigure(0, weight=4)
    window.grid_columnconfigure(1, weight=4)
    window.grid_columnconfigure(2, weight=1)
    window.grid_rowconfigure(0, weight=2)
    window.grid_rowconfigure([1, 2, 3, 4, 5, 6, 7], weight=1)
    add_input_file_upload()
    add_elements()

def run_texts(run_button, progress_bar):
    progress_bar.grid(row=6, column=2, padx=10, pady=10, sticky="nsew")
    progress_bar["value"] = 0
    progress_bar["maximum"] = 100

    run_button.config(state="disabled")
    number_files = len(os.listdir(INPUT_PATH))
    step = 100 / number_files
    for file in os.listdir(INPUT_PATH):
        read_and_write_file(mode_func, file)
        progress_bar["value"] += step
        progress_bar.update()
    run_button.config(state="normal")
    progress_bar.grid_remove()

def change_mode(new_mode, button, input_box, output_box, run_button):
    global mode_func
    global prev_button
    if new_mode == mode_func:
        return
    run_button.config(state="normal")
    button.config(relief="sunken")
    if prev_button is not None:
        prev_button.config(relief='raised')
    prev_button = button
    mode_func = new_mode
    original_sen, output_sen = run_first_sentence()
    change_text(original_sen, input_box, output_sen, output_box)

def run_first_sentence():
    first_sentence = get_first_sentence()
    if mode_func == word_frequency:
        output_sentence = mode_func(first_sentence, True)
        return first_sentence, output_sentence
    output_sentence = mode_func(first_sentence)
    return first_sentence, output_sentence

def change_text(input_text, input_box, output_text, output_box):
    input_box.config(text=input_text)
    output_box.config(text=output_text)

def file_upload_request(frame):
    upload_file()
    for widget in frame.winfo_children():
        widget.destroy()
    i = 0
    for file in os.listdir(INPUT_PATH):
        tk.Label(frame, text=file).grid(row=i, column=0, sticky="w")
        i += 1

window = tk.Tk()

create_gui()

window.mainloop()