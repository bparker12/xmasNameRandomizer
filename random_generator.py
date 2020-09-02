import random
import time
from email_build import buildEmail
from confirmation_email import buildKeyEmail
from lsts import giver_list, key_master

giver = giver_list

receiver = [name for name in giver]

# this function randomly chooses a int within the range of the list provided an removes it from the list
def pop_random(lst):
        idx = random.randrange(0, len(lst))
        return lst.pop(idx)

# loops through list and removes similar "pairing" of current item in list, adds the pair to a dictionary and then adds back in the "pairing" after the email is sent
pairs = {}

def randomize_pairs(list1, list2):
    for counter, name in enumerate(list1):
        findPairing = name['pairing']
        pairingMatch = [x for x in list2 if x['pairing'] == findPairing]
        for person in pairingMatch: 
            list2.remove(person)
        chosenPerson = pop_random(list2)
        for person in pairingMatch:
            list2.append(person)
        pairs[counter+1] = {"giver": name['name'], "email": name['email'], "receiver": chosenPerson['name'],}

# loops over pairs and sends email based on info provided
def sendEmail(match):
    for p_Id, p_info in match.items():
        buildEmail(p_info['giver'], p_info['email'], p_info['receiver'])

working = False
# this while function will only work if no exception is thrown, which in this case is when the last person matches with a similar pairing.  It will auto restart the function until it completes without the exception
while not working:
    try:
        randomize_pairs(giver, receiver)
        sendEmail(pairs)
        buildKeyEmail(pairs, key_master)
        working = True
    except ValueError as e:
    # the receiver reset is needed, otherwise the randomize_pairs() function doesn't work.  All dictionaries are removed after function is run
        receiver = [name for name in giver]
        print(e)
        pass