# csci5832-final-project

By:
Jasper Wilkerson & Nick Derby

# Use Case:

This tool is intended for linguistic researchers who want to use Natural Language ToolKit's features, but do not have the necessary time, expertise, or resources to do so. This tool can preform Tokenization, sentence detection, part-of-speech tagging, word frequency, lemmatization and named entity recognition on raw text documents.

# How to use:

## Starting the tool

There are two ways to start the NLTK Visual Tool.

1.  It can be run as an exe. Inside the folder Project_Distribution, there is a file called "NLTK_Visual_Tool.exe". Running this exe will open the NLTK Visual Tool window.

2.  The NLTK Visual Tool can also be manually run by running the gui.py script. To install the necessary packages, run the following lines in terminal.

        python NLTK_downloads.py
        pip install -r requirements.txt

Once these are installed, you can run the NLTK Visual Tool with

    python gui.py

## Using the tool

Once the window has been opened, select the Upload File button and select the appropriate txt or PDF file. If you are using the .exe version, files can also be manually placed in the "input" folder. Then, select the desired option from the menu on the right. You should see a preview populate on the left hand side, demonstrating what the output would look like using the first sentence from the first file. If this preview looks correct, select the Run button. This will run the selected option on all files (files can be viewed in the miniviewer located next to the Upload Button). You should see a progress bar to indicate program progression. To download your completed files, press the download button. This will create a folder called "Output" in your downloads, containing annotated .txt files.

# Options:

- Part of Speech Tagging
  This option tags each word with its respective part of speech. Abbreviations can be found here: https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html

- Word Frequency
  This option counts the occurence of words in the dataset, sorted from most to least frequent.

- Lemmantization
  This option extracts the lemma of each word, ie. the basic meaning of the word. For example, "singing" would become "sing".

- Named Entity Recognition
  This option extracts the named entities from the document. The categories are GPE (Geopolitical Entity), Organization, Person, and Location

# Object Oriented Principles

This project is mainly based around encapsulation of the technical requirements when using NLTK. The code is meant to be easy to understand and simplified. Other object oriented principles are applied in this project are: 

Model View Controller demonstrated by the separate GUI and languageProcessing scripts which are mediated mainly through fileReader. 
Strategy Pattern which can be seen in the switching of the mode_func parameter. At runtime, the strategy for the run function can be changed depending on the user's input. 
Builder pattern is also loosly used in tkinter (the GUI platform), where elements are created iteratively and added to the grid, then the window is created. 

Challenges:
Because python has only public variables, it was a challenge to effectively keep variables private. Tkinter (the GUI platform) also encourages and expects public variables. For example, labels and boxes are typically public and not created inside a function, but in the main script so accessing them for the purpose of updating them while maintaining private (ish) variables proved to be a challenge. However, by passing the objects to the functions in the GUI, we could effectively keep variables private and to one single instance (making a pseudo singleton pattern). 

# Notes for Graders

Unit testing can be found in "unit_testing.ipynb".

Some bugs may occur when uploading files due to mac/windows/linux differences.
