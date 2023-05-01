# Author: Ayelet Zadock
# Last modified: May 01 2023

# Imports:
from flask import Flask, render_template, request, flash, redirect, url_for
from CalculateStatus import calculate_status as cs
from CalculateStatus import add_flight, update_csvfile, get_data_by_flightID, get_csvfile

# Create app
app = Flask(__name__, template_folder='')
app.secret_key = "asdfghj"

@app.route('/')
def run_homepage():
    '''
    A function to run HTML page.
    :return: HTML file.
    '''
    return render_template('./home.html')


@app.route('/add_flight', methods=['POST'])
def update_flights():
    '''
    A function to update flight in CSV file and update flights status.
    :return: Redirect to homepage.
    '''
    if request.method == 'POST':
        # Get data from HTML post form
        flight_id = request.form.get('flightID')
        arrival = request.form.get('arrival')
        departure = request.form.get('departure')

        # Add the new flight to CSV file
        status = add_flight(flight_id, arrival, departure)
        if status:
            print("New flight was added successfully")

        # Update status of flights
        dataFrame = cs()
        update_status = update_csvfile(dataFrame)
        flash(update_status)  # update message in HTML file message box
        return redirect(url_for('run_homepage'))


@app.route('/get_flight', methods=['GET'])
def get_flight_details():
    '''
    A function to get flight status by flight id.
    :return: Redirect to homepage.
    '''
    if request.method == 'GET':
        flight_id = request.args.get('flightID_get')
        status = get_data_by_flightID(flight_id)
        flash(status)  # update message in HTML file message box
        return redirect(url_for('run_homepage'))

# The next function does not work due to memory error (too many runs)
@app.route('/get_data', methods=['GET'])
def get_csvfile():
    '''
    A function to get CSV file in text format.
    :return: Redirect to homepage.
    '''
    if request.method == 'GET':
        csvfile = get_csvfile()
        status = get_data_by_flightID(csvfile)
        flash(status)  # update message in HTML file message box
        return redirect(url_for('run_homepage'))


if __name__ == '__main__':
    app.run(host='localhost', debug=True)
