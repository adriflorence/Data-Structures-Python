import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def countDifferentPhoneNumbers(records):
    numberSet = set()
    for record in records:
        numberSet.add(record[0])
        numberSet.add(record[1])
    return len(numberSet)

def printAnswer(count):
    answer = "There are {} different telephone numbers in the records.".format(count)

uniqueNumbers = countDifferentPhoneNumbers(calls) +  countDifferentPhoneNumbers(texts)
print(uniqueNumbers)
