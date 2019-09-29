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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def printTelephoneNumbersCount():
    uniquePhones = set()
    for call in calls:
        incomingNumber, answeringNumber, _, _  = call
        uniquePhones.add(incomingNumber)
        uniquePhones.add(answeringNumber)
    
    for text in texts:
        incomingNumber, answeringNumber, _ = text
        uniquePhones.add(incomingNumber)
        uniquePhones.add(answeringNumber)
    count = len(uniquePhones)
    print(f"There are <{count}> different telephone numbers in the records.");
    return None


printTelephoneNumbersCount()