import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def codesCalledFromBangalore(calls):
  codes = set()
  for call in calls:
    if("(080)" in call[0]):
      if(isMobile(call[1])):
        codes.add(getMobileCode(call[1]))
      elif():
        codes.add(getFixedCode(call[1]))

  #  The list of codes should be printed out one per line in lexicographic order with no duplicates.
  return sorted(list(codes))
   

def isMobile(number):
  return " " in number

def getMobileCode(number):
  return number[:4]

def getFixedCode(number):
  num = number.split(")")
  return num[1:]

def printCodes(codes):
  print("The numbers called by people in Bangalore have codes:")
  for code in codes:
    print(code)

# Part A:
codes_list = codesCalledFromBangalore(calls)
printCodes(codes_list)


# Part B:

"""
Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
