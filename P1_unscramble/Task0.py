import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def printRecordAtIndex(list, type, index):

    if(type == "text"):
        answer = "First record of texts, {} texts {} at time {}".format(list[index][0], list[index][1], list[index][2])
    elif(type == "call"):
        answer = "Last record of calls, {} calls {} at time {}, lasting {} seconds".format(list[index][0], list[index][1], list[index][2], list[index][3])
    print(answer)

printRecordAtIndex(texts, "text", 0)
printRecordAtIndex(calls, "call", -1)