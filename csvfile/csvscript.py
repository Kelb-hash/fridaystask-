import csv
import os
import sys

#read phone numbers from txt file


with open(os.path.join(sys.path[0], 'phone_numbers.txt'), 'r') as file:
    phone_numbers = file.read().splitlines()

#write phone numbers to CSV file
with open('phone_numbers.csv', 'w', newline='/n') as file:
    writer = csv.writer(file)
    for phone_number in phone_numbers:
        writer.writerow([phone_number])


