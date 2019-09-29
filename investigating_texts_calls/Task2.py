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
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def printLongestTimeOnPhone():
    phoneWithMaxDuration, phonesDuration, maxDuration = '', {}, 0
    for call in calls:
        incomingNumber, answeringNumber, duration, _  = call
        addPhoneDuration(incomingNumber, duration, phonesDuration)
        addPhoneDuration(answeringNumber, duration, phonesDuration)
        phoneWithMaxDuration = getPhoneWithMaxDuration(incomingNumber, answeringNumber, phoneWithMaxDuration, phonesDuration)
    print(f"<{phoneWithMaxDuration}> spent the longest time, <{phonesDuration[phoneWithMaxDuration]}> seconds, on the phone during September 2016.")
    return maxDuration

def addPhoneDuration(phone, duration, dictionary):
    if dictionary.get(phone):
        dictionary[phone] += duration
    else:
        dictionary[phone] = duration
    
def getPhoneWithMaxDuration(*args, ds):
    maxDurationPhone = ''
    for arg in args:
        None
    return maxDurationPhone

printLongestTimeOnPhone()