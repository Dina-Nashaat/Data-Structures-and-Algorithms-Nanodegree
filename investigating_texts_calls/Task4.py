from helpers.Task3 import insertLexicographic

"""
Read file into texts and calls.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


def identifyPossibleTelemarketers():
    uniquePhones = set()
    possibleTelemarketers = []
    for text in texts:
        incomingNumber, answeringNumber, _ = text
        uniquePhones.add(incomingNumber)
        uniquePhones.add(answeringNumber)

    for call in calls:
        _, answeringNumber, _, _  = call
        uniquePhones.add(answeringNumber)

    for call in calls:
        incomingNumber, _, _, _  = call
        if incomingNumber not in uniquePhones:
            insertLexicographic(incomingNumber, possibleTelemarketers)
    
    print("These numbers could be telemarketers: ")
    print('\n'.join(map(str, possibleTelemarketers))) 
