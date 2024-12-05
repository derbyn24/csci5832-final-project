# csci5832-final-project

By:
Jasper Wilkerson
Nick Derby

Use Case:

This tool is intended for linguistic researchers who want to use Natural Language ToolKit's features, but do not have the necessary time, expertise, or resources to do so. This tool can preform Tokenization, sentence detection, part-of-speech tagging, word frequency, and lemmatization on raw text documents. 

How to use:
[PUT HOWEVER YOU START THE TOOL HERE]. In the window, select the Upload File button and select the appropriate txt [OR PDF?] file. Then, select the desired option from the menu on the right. You should see a preview populate on the left hand side, demonstrating what the output would look like using the first sentence from the first file. If this preview looks correct, select the Run button. This will run the selected option on all files (which can be viewed in the miniviewer located next to the Upload Button). You should see a loading bar indicating progress [IF THIS GETS IMPLEMENTED]. [PUT HOWEVER USERS WILL ACCESS FILES HERE, DOWNLOAD?]


//notes (to be deleted)

I'm starting to draft my functions in a notebook just so they can easily be run and tested, but probably we'll have to migrate them to a regular python file eventually.

GUI Plans: my plan so far for the gui is that users will select whichever "mode" they want to use, and it'll display a sample output on the first sentence of the first file to show what the output would look like, then a user will hit run to analyze all the files. I feel like it would be nicer to see an example output before spending a lot of time running files. 

I'd also like to do a progress bar while the files are running if possible but tkinter is annoying to work with thus far so we'll see. 

TODO's: 

- [ ] Make it so that uploading files updates the file list

- [ ] fully implement "run" logic 

- [ ] add a "download" button so that users can download the "output" folder to their computer rather than having to mess with internal files

- [ ] potentially package this in some way, website, exe or something else

- [ ] potentially implement chunking? or adding other nltk functions

- [ ] figure out formatting of the output

- [ ] make gui code cleaner?

    - [ ] fix gui so textbox is a consistent size and text wraps

    - [ ] progress bar??

    - [ ] move code logic out of gui? Should probably be Model/View/Controller pattern
