import re

"""
search a sorted list for a value
return True if value found and its index
return False if value not found and its exact index if added
"""
def searchAndGetIndex(code, codes, prevMid = 0):
  if len(codes) == 1:
    if code == codes[0]:
      return True, prevMid
    elif code < codes[0]:
      return False, prevMid
    elif code > codes[0]:
      return False, prevMid + 1
  mid = len(codes) // 2

  if code >= codes[mid]:
    return searchAndGetIndex(code, codes[mid:], mid + prevMid)
  else:
    return searchAndGetIndex(code, codes[:mid], prevMid)

"""
Insert a value into a sorted array
"""
def insertLexicographic(value, sortedArray):
  if len(sortedArray) == 0:
    sortedArray.append(value)
    return
  found, index = searchAndGetIndex(value, sortedArray)
  if not found:
    sortedArray.insert(index, value)

"""
Get specific area code from phone number
"""
def getAreaCode(phone):
  if isMobileNumber(phone):
    return phone.split(' ')[0][:4]
  if isTelemarketersNumber(phone):
    return 140
  if isFixedLine(phone):
    return phone[phone.find("(")+1:phone.find(")")]
  raise Exception('Cannot identify this phone number', phone)
  
"""
return true if phone has (080) code
"""
def isBangaloreFixedLine(phone):
  bangaloreFixedLinePattern = re.compile(r'^\(080\)[0-9]+')
  return bool(bangaloreFixedLinePattern.match(phone))

"""
return true if phone has space inbetween and starts with 7, 8, 9
"""
def isMobileNumber(phone):
  mobileNumberPattern = re.compile(r'^(7|8|9)\d{3,} \d+')
  return bool(mobileNumberPattern.match(phone))

"""
return true if number starts with 140
"""
def isTelemarketersNumber(phone):
  telemarketerNumberPattern = re.compile(r'^140\d+')
  return bool(telemarketerNumberPattern.match(phone))

"""
return true if starts with brackets and has area code that starts with 0
"""
def isFixedLine(phone):
  fixedLinePattern = re.compile(r'^\(0[0-9]+\)[0-9]+')
  return bool(fixedLinePattern.match(phone))
