# ROR2-Randomiser

Generate a random loadout for a run of Risk of Rain 2



Activate .py file will generate a text file with a survivor with a randomised build in order that they appear in game.

For example:

1

2

2

1

is the equivalent of picking Option 1 in Row 1, Option 2 in Row 2, Option 2 in Row 3 and Option 1 in Row 4.



Also generates a random skin to use.



============================================

###### **INSTALLATION**
Dependencies are located in 'requirements.txt'
Using pip install -r requirements.txt will install libraries automatically
	Should only be numpy

###### **FLAGS**

The command line flags can be used to specify conditions:

-f -> Adds a randomised finale to the file (Default = False)

-s <survivor> -> Randomises a specific survivor (If not specified will randomly choose a survivor)



e.g.: py path\\to\\folder\\ror2.py -f -s acrid

&nbsp;	Will give a randomised acrid run

