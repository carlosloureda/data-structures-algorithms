"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
def getTelephonesInArray(phoneSet, arr):
    for elem in arr:
        phoneSet.add(elem[0])
        phoneSet.add(elem[1])
    return phoneSet

phoneSet = set([])
phoneSet = getTelephonesInArray(phoneSet, texts)
phoneSet = getTelephonesInArray(phoneSet, calls)

print("phone set length: ", len(phoneSet))
