import csv
import operator

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

### TASK 2
# Which telephone number spent the longest time on the phone
# during the period? Note that time spent answering a call is
# also time spent on the phone.

def get_numbers_with_durations(calls): # O(n)
    call_dict = dict()
    for call in calls:
        if(call[0] not in call_dict):
            # if number is not in dict, add it with duration
            call_dict[call[0]] = int(call[3])
        else:
            # if number is in dict, update duration
            call_dict[call[0]] += int(call[3])

        if(call[1] not in call_dict):
            # if number is not in dict, add it with duration
            call_dict[call[1]] = int(call[3])
        else:
            # if number is in dict, update duration
            call_dict[call[1]] += int(call[3])
    return call_dict

def get_longest_converstation(call_dict): # O(n)
    return max(call_dict.iteritems(), key=operator.itemgetter(1))

def print_longest_conversation(longest): # O(1)
    number, duration = longest[0], longest[-1]
    answer = "{} spent the longest time, {} seconds, on the phone during September 2016.".format(number, duration)
    print(answer)

call_dict = get_numbers_with_durations(calls)
longest = get_longest_converstation(call_dict)
print_longest_conversation(longest)