"""
Read file into texts and calls.
"""
import csv
with open('./investigating_texts_calls/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('./investigating_texts_calls/calls.csv', 'r') as f:
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
    phoneWithMaxDuration, phonesDuration = '', {}
    for call in calls:
        incomingNumber, answeringNumber, _, duration  = call
        addPhoneDuration(incomingNumber, duration, phonesDuration)
        addPhoneDuration(answeringNumber, duration, phonesDuration)
        phoneWithMaxDuration = getPhoneWithMaxDuration(
            [incomingNumber, answeringNumber, phoneWithMaxDuration],
            phonesDuration
        )
    print(f"<{phoneWithMaxDuration}> spent the longest time, <{phonesDuration[phoneWithMaxDuration]}> seconds, on the phone during September 2016.")

def addPhoneDuration(phone, duration, ds):
    if ds.get(phone):
        ds[phone] += int(duration)
    else:
        ds[phone] = int(duration)
    
def getPhoneWithMaxDuration(phones, ds):
    maxDurationPhone = ''
    for phone in phones:
        duration = ds.get(phone)
        maxDuration = ds.get(maxDurationPhone)
        if not maxDuration:
            maxDurationPhone = phone
        elif duration:
            maxDurationPhone = phone if duration > maxDuration else maxDurationPhone
    return maxDurationPhone

assert(getPhoneWithMaxDuration(
    ['123', '443', '555', ''], 
    {'123': 4, '443': 5, '555': 17}) == '555' 
)

printLongestTimeOnPhone()
