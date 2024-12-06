# csci5832-final-project

By:
Jasper Wilkerson
Nick Derby

Use Case:

This tool is intended for linguistic researchers who want to use Natural Language ToolKit's features, but do not have the necessary time, expertise, or resources to do so. This tool can preform Tokenization, sentence detection, part-of-speech tagging, word frequency, and lemmatization on raw text documents. 

How to use:
[PUT HOWEVER YOU START THE TOOL HERE]. In the window, select the Upload File button and select the appropriate txt or PDF file. Then, select the desired option from the menu on the right. You should see a preview populate on the left hand side, demonstrating what the output would look like using the first sentence from the first file. If this preview looks correct, select the Run button. This will run the selected option on all files (files can be viewed in the miniviewer located next to the Upload Button). You should see a progress bar to indicate program progression. To download your completed files, press the download button. This will create a folder called "Output" in your downloads, containing annotated .txt files. 

Options:
- Part of Speech Tagging
    This option tags each word with its respective part of speech. Abbreviations can be found here: https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html

- Word Frequency
    This option counts the occurence of words in the dataset, sorted from most to least frequent. 

- Lemmantization
    This option extracts the lemma of each word, ie. the basic meaning of the word. For example, "singing" would become "sing".

- Chunking
    [TBD]


TODO's: 

- [ ] figure out formatting of the output

- [ ] package this in some way, website, exe or something else

- [ ] potentially implement chunking? or adding other nltk functions

- [ ] make gui code cleaner and potentially look nicer?

    - [ ] move code logic out of gui? Should probably be Model/View/Controller pattern
