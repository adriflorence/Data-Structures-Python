import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def count_different_phone_numbers(records): # O(n)
    numberSet = set()
    for record in records:
        numberSet.add(record[0])
        numberSet.add(record[1])
    return len(numberSet)

def print_answer(count): # O(1)
    answer = "There are {} different telephone numbers in the records.".format(count)

records = calls + texts
unique_numbers = count_different_phone_numbers(records)
print_answer(unique_numbers)
