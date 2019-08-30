# ProxyDecks
Create a printable pdf of cards for making a proxy deck

This is built for Dragon Ball Super cards, but can easily be changed to use any set of pictures or other card games added. 

## Licensing

Please share your improvements so everyone can benefit! Feel free to post pull requests to improve this script.

## How to run

Download the repository. Easiest method is probably downloading GitHub for Desktop for a graphical interface to pull the files. Or you can download the repo as a zip file, but if there are changes you will have to redownload the entire folder.

Write your cards into CardList.txt, there is an example deck populated. The format reads dbs-decks.com's export to txt format, so you can just copy paste that file. The only text that matters is a number followed by a card ID on the same line. All the other text, such as the name of the card, is ignored and can be left out. A minimally formatted input file will be generated when you run the program, CardList_Formatted.txt, that can also be pasted into CardList.txt for input. Lastly, a pdf of your cards, Cards.pdf, will be written to the folder.

A leader's back will be automatically included if the front is listed, use --no_leader_back to prevent this. To only print the back, simply write the card id for the back. 

### Method 1

Install Python 3

Add the python executable folder to your path

Navigate to the top level ProxyDecks folder in a command prompt

Run `pip3 install Pillow`

Run `python proxy.py`

(Might need to install a couple other packages. Just read the error message and pip3 install that package too)

### Method 2 (no python installed)

Navigate to the top level ProxyDecks folder in a command prompt.

Run `.\proxy\proxy.exe`

![how_to_run](how_to_run.gif)

## Options

`-h` to see the options

`--lower_res` to use the lower resolution cards in the Cards_lower_res folder. These are much smaller in size and the program runs faster. Not recommended unless you need to for some reason.

`--no_leader_back` to prevent the back of the leader card being automatically added after a leader front is included. 
