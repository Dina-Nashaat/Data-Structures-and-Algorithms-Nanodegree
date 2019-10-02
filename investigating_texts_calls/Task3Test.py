import unittest
from helpers.Task3 import isMobileNumber, \
  isBangaloreFixedLine, isFixedLine, \
  isTelemarketersNumber, searchAndGetIndex

class TestTask3(unittest.TestCase):

  def test_IsMobileNumber(self):
    assert(isMobileNumber('4567 8908') == False)
    assert(isMobileNumber('78373 8908') == True)
    assert(isMobileNumber('883733 8908') == True)
    assert(isMobileNumber('9837 8908') == True)
    assert(isMobileNumber('14099305') == False)
    assert(isMobileNumber('(080)898393') == False)

  def test_IsBangaloreFixedLine(self):
    assert(isBangaloreFixedLine('(080)898393') == True)
    assert(isBangaloreFixedLine('(090)89388493') == False)
    assert(isBangaloreFixedLine('14099305') == False)

  def test_IsFixedLine(self):
    assert(isFixedLine('(009)898393') == True)
    assert(isFixedLine('(909)898393') == False)
    assert(isFixedLine('8938 8493') == False)
    assert(isFixedLine('140989305') == False)

  def test_IsTelemarketersNumber(self):
    assert(isTelemarketersNumber('4567 8908') == False)
    assert(isTelemarketersNumber('14099305') == True)
    assert(isTelemarketersNumber('140') == False)
    assert(isTelemarketersNumber('15099305') == False)
    assert(isTelemarketersNumber('(080)898393') == False)

  def test_SearchAndGetIndex(self):
    arr = [2, 4, 5, 12, 18, 19, 50]
    assert(searchAndGetIndex(1, arr) == (False, 0))
    assert(searchAndGetIndex(5, arr) == (True, 2))
    assert(searchAndGetIndex(50, arr) == (True, 6))  
    assert(searchAndGetIndex(15, arr) == (False, 4))

if __name__ == '__main__':
    unittest.main()