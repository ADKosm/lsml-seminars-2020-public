import sys
import csv

vehicle_count = 0
record_count = 0

for record in csv.reader(iter(sys.stdin.readline, '')):
    current_vehicle_count = int(record[6])
    vehicle_count += current_vehicle_count
    record_count += 1

print(vehicle_count / record_count)
