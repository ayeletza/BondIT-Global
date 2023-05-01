# Author: Ayelet Zadock
# Last modified: April 30 2023

# Imports:
from Globals import *

rows = [
    ['flight ID', 'Arrival', 'Departure', 'success'],
    ['A12', '09:00', '13:00', ''],
    ['A14', '12:00', '19:00', ''],
    ['B15', '10:00', '13:00', ''],
    ['C124', '14:00', '16:00', ''],
    ['C23', '08:00', '17:00', ''],
    ['B12', '13:01', '16:00', ''],
    ['G56', '09:30', '14:00', ''],
    ['B35', '16:01', '20:00', ''],
    ['A21', '08:00', '13:00', ''],
    ['A19', '17:00', '19:00', ''],
    ['B55', '11:00', '13:00', ''],
    ['C128', '12:00', '16:00', ''],
    ['C26', '08:00', '17:00', ''],
    ['B52', '12:01', '16:00', ''],
    ['G86', '07:30', '14:00', ''],
    ['B65', '7:01', '20:00', ''],
    ['B05', '10:00', '14:00', ''],
    ['C1223', '12:55', '16:00', ''],
    ['C235', '08:00', '22:00', ''],
    ['B46', '14:01', '16:00', ''],
    ['G88', '09:30', '14:00', ''],
    ['B39', '16:01', '20:00', ''],
    ['G88', '11:30', '14:05', ''],
    ['B39', '16:01', '20:00', '']
]

# Create a new file and set the raw data
with open(file_name, 'w', newline='') as flights_file:
    writer = csv.writer(flights_file)

    for row in rows:
        try:
            flight_id, arrival, departure, success = row
            arrival = datetime.strptime(arrival, time_format).time()  # convert to time format
            departure = datetime.strptime(departure, time_format).time()  # convert to time format
            writer.writerow([flight_id, arrival, departure, success])
        except:
            writer.writerow(row)
