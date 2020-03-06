import csv

# Read from files
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# Returns a list of area codes that were called from a given area code
# In lexicographic order with no duplicates
def codesCalledFromCode(calls, code): # O(n)
  codes = set()
  for call in calls:
    if(code in call[0]):
      if(isMobile(call[1])):
        codes.add(getMobileCode(call[1]))
      elif():
        codes.add(getFixedCode(call[1]))

  return sorted(list(codes))
   

def isMobile(number): # O(1)
  return " " in number

def getMobileCode(number): # O(1)
  return number[:4]

def getFixedCode(number): # O(1)
  num = number.split(")")
  return num[1:]

# Print area codes one per line
def printCodes(codes): # O(1)
  print("The numbers called by people in Bangalore have codes:")
  for code in codes:
    print(code)


# Part A:
codes_list = codesCalledFromCode(calls, "(080)")
printCodes(codes_list)

########################################

def callsFromAreaCode(calls, code): # O(n)
  calls_from_area = []
  for call in calls:
    if(code in call[0]):
      calls_from_area.append(call)
  return calls_from_area

def callsToAreaCode(calls, code): # O(n)
  calls_to_area = []
  for call in calls:
    if(code in call[1]):
      calls_to_area.append(call)
  return calls_to_area

# Calculates percentage with decimal digits
def calculatePercentage(total, fraction): # O(1)
  percentage = (fraction * 100.0) / total
  return round(percentage, 2)


def printPercentage(percentage): # O(1)
  answer = "{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentage)
  print(answer)


# Part B:
calls_from_area = callsFromAreaCode(calls, "(080)") # all 080 calls
calls_to_area = callsToAreaCode(calls_from_area, "(080)") # 080 to 080 calls
percentage = calculatePercentage(len(calls_from_area), len(calls_to_area))
printPercentage(percentage)