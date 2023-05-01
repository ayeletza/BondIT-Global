# Author: Ayelet Zadock
# Last modified: May 01 2023

# Imports:
import pandas as pd
from Globals import *

# Each line in csv file says the arrival time of the flight,
# then, when the flight leaves (departure time)

# Functions:
def calculate_status():
    '''
    A function to calculate the status of each flight,
    depends on arrival and departure times, and depends on amount of flights in day.
    :return: A dataFrame
    '''
    # DataFrame to read our input CSV file
    dataFrame = pd.read_csv(file_name)

    # sorting by Arrival column
    dataFrame.sort_values(by='Arrival', axis=0, ascending=True, inplace=True, na_position='first')

    # Convert times in SCV file from str to timedelta
    arrival = pd.to_timedelta(dataFrame['Arrival'])
    departure = pd.to_timedelta(dataFrame['Departure'])
    delta = departure - arrival

    counter = 0
    for index in delta.index:
        # Check condition to 'success', and set dataFrame success status
        if counter < MAX_SUCCESS and delta[index].total_seconds() / NUM_SECONDS_IN_A_MIN >= wait_time:
            dataFrame.loc[index, 'success'] = 'success'
            counter += 1
        else:
            dataFrame.loc[index, 'success'] = 'fail'

    return dataFrame


def update_csvfile(dataFrame):
    '''
    A function to update the CSV file with the given data.
    :param dataFrame: A given data to update.
    :return: A message of status of function.
    '''
    try:
        # reading the csv file
        df = pd.read_csv(file_name)

        for index in dataFrame.index:
            # updating the column value/data
            df.loc[index, 'success'] = dataFrame.loc[index, 'success']

        # writing into the file
        df.to_csv(file_name, index=False)

        return "CSV file updated successfully"
    except:
        return "Failed to update CSV file"


def add_flight(flight_id, arrival, departure):
    '''
    A function to add a new flight to CSV file.
    :param flight_id: flight id
    :param arrival: arrival time
    :param departure: departure time
    :return: True if adding succeeded, False otherwise.
    '''
    # Open the CSV file to update
    with open(file_name, 'a', newline='') as flights_file:
        writer = csv.writer(flights_file)

        try:
            arrival = datetime.strptime(arrival, time_format).time()  # convert to time format
            departure = datetime.strptime(departure, time_format).time()  # convert to time format
            writer.writerow([flight_id, arrival, departure, ''])
            return True
        except:
            print("Error occurred while adding a new flight")
            return False


def get_data_by_flightID(flight_id):
    '''
    A function to get flight status by flight id.
    :param flight_id: flight id.
    :return: flight status if exists, error text message otherwise.
    '''
    # DataFrame to read our input CSV file
    dataFrame = pd.read_csv(file_name)
    flight_details = dataFrame.loc[dataFrame['flight ID'] == flight_id]
    # Check if flight exists
    if flight_details.count().sum() > 0:
        flight_status = f"Flight {flight_id} status is {flight_details['success'].values[0]}"
        return flight_status
    else:
        return f"There is no data about flight ID {flight_id}"


def get_csvfile():
    '''
    A function to get CSV file as a string.
    :return: A string that contains all data in CSV file. Error message if error occurred.
    '''
    try:
        # reading the csv file
        df = pd.read_csv(file_name)
        # print(df.to_json())
        str_df = 'flight ID\tArrival\tDeparture\tsuccess\n'

        for index in df.index:
            # coping the column value/data
            temp_str = f"{df.loc[index, 'flight ID']}\t\t" \
                f"{df.loc[index, 'Arrival']}\t\t" \
                f"{df.loc[index, 'Departure']}\t\t" \
                f"{df.loc[index, 'success']}\n"
            str_df += temp_str

        return str_df
    except:
        return "Failed to read CSV file"

# Runs examples:
# print(get_csvfile())
# print(get_data_by_flightID('A12'))
# df = calculate_status()
# update_csvfile(df)
