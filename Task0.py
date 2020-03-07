import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def print_record_at_index(records, record_type, index): # O(1)

    if(record_type == "text"):
        answer = "First record of texts, {} texts {} at time {}".format(records[index][0], records[index][1], records[index][2])
    elif(record_type == "call"):
        answer = "Last record of calls, {} calls {} at time {}, lasting {} seconds".format(records[index][0], records[index][1], records[index][2], records[index][3])
    print(answer)

print_record_at_index(texts, "text", 0)
print_record_at_index(calls, "call", -1)