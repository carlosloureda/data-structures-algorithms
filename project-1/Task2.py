"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

"""
1. Inputs are: calls file(calling number, answering number, start time, duration)
2. Outputs: tuple(number, seconds), telephone number and seconds
3.
"""


def get_phone_number_statistics(calls):
    phone_numbers = {}
    for line in calls:
        phone_number_1, phone_number_2, time, seconds = line
        seconds = int(seconds)
        if phone_number_1 not in phone_numbers:
            phone_numbers[phone_number_1] = [phone_number_1, seconds]
        else:
            phone_numbers[phone_number_1][1] = int(
                phone_numbers[phone_number_1][1]) + seconds
        if phone_number_2 not in phone_numbers:
            phone_numbers[phone_number_2] = [phone_number_2, seconds]
        else:
            phone_numbers[phone_number_2][1] = int(
                phone_numbers[phone_number_2][1]) + seconds
    return phone_numbers


def biggest_seconds(phone_number_info):
    biggest = (0, 0)  # phone, seconds
    for info in phone_number_info:
        if int(phone_number_info[info][1]) > int(biggest[1]):
            biggest = (phone_number_info[info][0], phone_number_info[info][1])
    return biggest


def get_max_user_info(calls):
    phone_statistics = get_phone_number_statistics(calls)

    return biggest_seconds(phone_statistics)


phone_number, total_time = get_max_user_info(calls)
print(f"{phone_number} spent the longest time, {total_time} seconds, on the phone during September 2016.")
