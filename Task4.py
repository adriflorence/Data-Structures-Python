import csv

# Read from files
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


# Returns a list of calling telephone numbers with no duplicates
def telephoneNumbers(calls, index): # O(n)
    result = set()
    for call in calls:
        result.add(call[index])
    return result

# Returns a list of calling telephone numbers with no duplicates
def mobileNumbers(texts): # O(n)
    result = set()
    for text in texts:
        result.add(text[0])
        result.add(text[1])
    return result


# Returns a list of callers that never had incoming calls
def noIncomingCalls(callers, callees): # O(n)
    result = set()
    for caller in callers:
        if(caller not in callees):
            result.add(caller)
    return result

# Returns a list of caller numbers that does NOT appear in the texts.csv file
def noTexts(callers, mobiles): # O(n)
    result = set()
    for caller in callers:
        if(caller not in mobiles):
            result.add(caller)
    return result

def printTelemarketers(telemarketers): # O(n)
    for tm in telemarketers:
        print(tm)

# The telephone company want to identify numbers that might be doing
# telephone marketing. Create a set of possible telemarketers:
# these are numbers that make outgoing calls but never send texts,
# receive texts or receive incoming calls.


callers = list(telephoneNumbers(calls, 0))
callees = list(telephoneNumbers(calls, 1))
mobiles = list(mobileNumbers(texts))
# print(len(callers))
# print(len(callees))
# print(len(mobiles))

callers_without_incoming_calls = noIncomingCalls(callers, callees)
callers_without_texts = noTexts(callers_without_incoming_calls, mobiles)
telemarketers = sorted(list(callers_without_texts)) # O(NlogN) slowest function
printTelemarketers(telemarketers)