from Task0 import printFirstTextRecord, printLastCallRecord
from Task1 import printTelephoneNumbersCount
from Task2 import printLongestTimeOnPhone
from Task3 import codesCalledByBangalore, bangaloreToBangaloreCallPercent
from Task4 import identifyPossibleTelemarketers

import sys

def main():
  args = sys.argv[1:]

  if('task0' in args or 'all' in args):
    print('Task 0')
    print('======================')
    printFirstTextRecord()

  if('task1' in args or 'all' in args):
    print('Task 1')
    print('======================')
    printTelephoneNumbersCount()

  if('task2' in args or 'all' in args):
    print('Task 2')
    print('======================')
    printLongestTimeOnPhone()

  if('task3A' in args or 'all' in args):
    print('Task 3 - Part A')
    print('======================')
    codesCalledByBangalore()
  
  if('task3B' in args or 'all' in args):
    print('Task 3 - Part B')
    print('======================')
    bangaloreToBangaloreCallPercent()
  
  if('task4' in args or 'all' in args):
    print('Task 4')
    print('======================')
    identifyPossibleTelemarketers()
  
if __name__== "__main__":
  main()
