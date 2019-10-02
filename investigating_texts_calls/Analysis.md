# BigO Analysis
__Note__: The following ignores the printing complexity in each function which should be O(n) where n is the length of the string

## Task 0:
**printFirstTextRecord**: 
Getting first item from list : **O(1)**
**printLastCallRecord**:
Getting last item from list : **O(1)**

## Task 1:
**printTelephoneNumbersCount**:
Looping over calls and texts records, and adding numbers in a set for each loop : **O(n + m)**
where n is the calls records length and m is the texts records length

## Task 2:
**printLongestTimeOnPhone**:
```
for call in calls: //(O(n))
    incomingNumber, answeringNumber, _, duration  = call
    addPhoneDuration(incomingNumber, duration, phonesDuration) // O(1)
    addPhoneDuration(answeringNumber, duration, phonesDuration) // O(1)
    phoneWithMaxDuration = getPhoneWithMaxDuration(
        [incomingNumber, answeringNumber, phoneWithMaxDuration],
        phonesDuration
    ) // O(m) where m is the number of arguments which is 3
```
Looping over calls and each time setting phone with maximum duration : **O(n)**

## Task 3:
**A - codesCalledByBangalore**: 
```
for call in calls: // O(n)
    incomingNumber, answeringNumber, _, _  = call
    if(isBangaloreFixedLine(incomingNumber)): //O(m) where m is string length to match
        insertLexicographic(getAreaCode(answeringNumber), codesList) //O(log(m) + m) -- Insertion with binary search
```
```
def insertLexicographic(value, sortedArray):
  if len(sortedArray) == 0:
    sortedArray.append(value)
    return
  found, index = searchAndGetIndex(value, sortedArray) \\O(log(n))
  if not found:
    sortedArray.insert(index, value) \\O(n)
```
for looping over calls and each time searching for value and inserting in the right place in a sorted array: O(n * (n + log(n))) => **O(n * m)** 
where n is the length of calls array and m is the length of unique sorted array

**B - bangaloreToBangaloreCallPercent**
```
incomingBangaloreCount = 0
answeringBangaloreCount = 0
for call in calls: // O(n)
    incomingNumber, answeringNumber, _, _  = call
    if isBangaloreFixedLine(incomingNumber): //O(m)
        incomingBangaloreCount += 1
        if(isBangaloreFixedLine(answeringNumber)):
        answeringBangaloreCount += 1
```
for looping over calls and checking each string against a regular expression: **O(n * m)**
where n is the number of calls and m is the lenght of number string

## Task 4A:
**identifyPossibleTelemarketers**:
```
for text in texts: \\ O(n)
    incomingNumber, answeringNumber, _ = text
    uniquePhones.add(incomingNumber) \\ O(1)
    uniquePhones.add(answeringNumber)

for call in calls: \\ O(m)
    _, answeringNumber, _, _  = call
    uniquePhones.add(answeringNumber)

for call in calls: \\ O(m)
    incomingNumber, _, _, _  = call
    if incomingNumber not in uniquePhones: \\ O(1)
        insertLexicographic(incomingNumber, possibleTelemarketers) \\O(k)
```
for looping over calls and texts to add phones to unique set: O(n + m)
for looping over calls and inserting in lexicographic order: O(m * k)
total complexity = O(n + m + m*k) = O(n + 2*m*k) = **O(n + m*k)**
