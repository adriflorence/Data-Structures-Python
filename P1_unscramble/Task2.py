import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


def calculateLongestConverstation(calls):
    longest = calls[0]
    for call in calls:
        if(int(call[-1]) > int(longest[-1])):
            longest = call
    return longest

def printLongestConversation(longest):
    number = longest[0]
    duration = longest[-1]
    answer = "{} spent the longest time, {} seconds, on the phone during September 2016.".format(number, duration)
    print(answer)

longest = calculateLongestConverstation(calls)
printLongestConversation(longest)