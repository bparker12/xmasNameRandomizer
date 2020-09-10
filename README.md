# Christmas Gift Exchange
This app was built to accommodate a gift exchange for Christmas in which all parties had a significant other that they should not match with.  

## GMAIL SetUp
I followed a tutorial and the GMAIL API docs to set up the API feature (i also did the quickstart tutorial [here](https://developers.google.com/gmail/api/quickstart/python)).

## Randomizer
The Randomizer uses the base python Random import to randomly choose an integer.  I utilized it to pick an integer in a list and bring back the result.  The tricky part was excluding the person that is currently going through the loop and their significant other. In order to achieve this, I included a dictionary key that would allow me to check this.  If they are a pair, I would remove them from a copied list and then add them in after the random was chosen.  

I did incur some errors in which the 2nd to last and last person would have any matches to pair with (only left with themselves or their significant other).  I included a non pythonic try and exception that would run until it doesn't have an error. 
