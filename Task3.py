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
def codes_called_from_code(calls, code): # O(n)
  codes = set()
  for call in calls:
    if(code in call[0]):
      if(is_mobile(call[1])):
        codes.add(get_mobile_code(call[1]))
      elif(is_telemarketer):
        codes.add('140')
      elif(is_fixed_line):
        codes.add(get_fixed_code(call[1]))
  return sorted(list(codes)) # O(NlogN)
   

def is_mobile(number): # O(1)
  if((" " in number) and number.startwith('7') or number.startwith('8') or number.startwith('9')):
    return True
  return False

def get_mobile_code(number): # O(1)
  return number[:4]

def is_telemarketer(number): # O(1)
  return number.startwith("140")

# Fixed lines start with an area code enclosed in brackets.
# The area codes vary in length but always begin with 0.
def is_fixed_line(number): # O(1)
  array_split = number.split(")")
  if array_split[0].startwith("(0"):
    return True
  return False

def get_fixed_code(number): # O(1)
  array_split = number.split(")")
  return array_split[0][1:]

# Print area codes one per line
def print_codes(codes): # O(1)
  print("The numbers called by people in Bangalore have codes:")
  print('\n'.join(codes))


# Part A:
codes_list = codes_called_from_code(calls, "(080)")
print_codes(codes_list)

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