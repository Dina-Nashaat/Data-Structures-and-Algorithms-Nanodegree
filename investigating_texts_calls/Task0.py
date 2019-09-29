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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

def printFirstTextRecord():
    incomingNumber, answeringNumber, time = texts[0]
    print(
        f"First record of texts, <{incomingNumber}> texts <{answeringNumber}> at time <{time}>"
    )
    return None

def printLastCallRecord():
    lastIndex = len(calls) - 1
    incomingNumber, answeringNumber, time, during = calls[lastIndex]
    print(
        f"Last record of calls, <{incomingNumber}> calls <{answeringNumber}> at time <{time}>, lasting <{during}> seconds"
    )
    return None

printFirstTextRecord()
printLastCallRecord()
print(len(calls))
print(len(texts))