# Excursion_booking_api

I have created an API to book holiday excursions through an agency. Users can view available excursions for a specific time frame, book an excursion or edit a previous booking. They can choose which tour guide they want and the time frame (24hr clock: 9-12, 13-18 or 19-23). When a booking is created or edited this will be reflected in the SQL file so that avilability is always up-to-date for the next user.

To use the API you must follow these steps:

Edit the config.py file to ensure HOST = "localhost", USER = "root" and PASSWORD = your own password for SQL.
Ensure you have imported json, requests, mysql.connector and flask.
Run the app.py file.
Run the main.py file alongside the app.py file.
Follow the interaction shown, answering the questions in the specified format until you reach the end of the booking(the DB connection will close when completed).
Enter the url http://localhost:5001/availability/"date" into your browser to view the availability for each specified date. E.g. http://localhost:5001/availability/2024-07-01.
