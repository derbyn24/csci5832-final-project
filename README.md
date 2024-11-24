# csci5832-final-project

By:
Jasper Wilkerson
Nick Derby

I'm starting to draft my functions in a notebook just so they can easily be run and tested, but probably we'll have to migrate them to a regular python file eventually.

GUI Plans: my plan so far for the gui is that users will select whichever "mode" they want to use, and it'll display a sample output on the first sentence of the first file to show what the output would look like, then a user will hit run to analyze all the files. I feel like it would be nicer to see an example output before spending a lot of time running files. 

I'd also like to do a progress bar while the files are running if possible but tkinter is annoying to work with thus far so we'll see. 

TODO's: 

- [ ] add code to copy a file to the input folder

- [ ] implement "run" logic 

- [ ] add a "download" button so that users can download the "output" folder to their computer rather than having to mess with internal files

- [ ] potentially package this in some way, website, exe or something else

- [ ] potentially implement chunking? or adding other nltk functions

- [ ] figure out formatting of the output

- [ ] make gui code cleaner?

    - [ ] fix gui so textbox is a consistent size and text wraps

    - [ ] progress bar??

    - [ ] move code logic out of gui? Should probably be Model/View/Controller pattern
