import random
from email import buildEmail

giver = [
    {"name": "Casie", "pairing": "a", "email": "superdummytest8679@gmail.com"},
    {"name": "Kyle", "pairing": "a", "email": "superdummytest8679@gmail.com"},
    {"name": "Ben", "pairing": "b", "email": "superdummytest8679@gmail.com"},
    {"name": "Meredith", "pairing": "b", "email": "superdummytest8679@gmail.com"},
    {"name": "Tyler", "pairing": "c", "email": "superdummytest8679@gmail.com"},
    {"name": "Alyssa", "pairing": "c", "email": "superdummytest8679@gmail.com"}]

receiver = [name for name in giver]

# this function randomly chooses a int within the range of the list provided an removes it from the list
def pop_random(lst):
        idx = random.randrange(0, len(lst))
        return lst.pop(idx)

# loops through list and removes similar "pairing" of current item in list and then sends an email to the person and then adds back in the "pairing" after the email is sent
def randomize_pairs(list1, list2):
    for name in list1:
        print("giver", name['name'])
        findPairing = name['pairing']
        pairingMatch = [x for x in list2 if x['pairing'] == findPairing]
        for name in pairingMatch:
            list2.remove(name)
        chosenPerson = pop_random(list2)
        print("chosenPerson", chosenPerson['name'])
        buildEmail(name, chosenPerson['name'])
        #send email with "name" as the recepient of email and the chosenPerson as the message body
        for name in pairingMatch:
            list2.append(name)


randomize_pairs(giver, receiver)