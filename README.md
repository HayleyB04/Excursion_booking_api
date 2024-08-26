# Excursion_booking_api

I have created an API to book holiday excursions through an agency. Users can view available excursions for a specific time frame, book an excursion or edit a previous booking. They can choose which tour guide they want and the time frame (24hr clock: 9-12, 13-18 or 19-23). When a booking is created or edited this will be reflected in the SQL file so that availability is always up-to-date for the next user.

![Screenshot 2024-08-26 152111](https://github.com/user-attachments/assets/a4c2ff3c-95ba-43eb-912d-a8f4cd65234d)

![Screenshot 2024-08-26 151753](https://github.com/user-attachments/assets/d5c83909-a1e2-4d68-a541-ccc0e43e86d6)

To use the API you must follow these steps:

- Edit the config.py file to ensure HOST = "localhost", USER = "root" and PASSWORD = your own password for SQL.
- Ensure you have imported json, requests, mysql.connector and flask.
- Run the app.py file.
- Run the main.py file alongside the app.py file.
- Follow the interaction shown, answering the questions in the specified format until you reach the end of the booking(the DB connection will close when completed).
- Enter the url http://localhost:5001/availability/"date" into your browser to view the availability for each specified date. E.g. http://localhost:5001/availability/2024-07-01.
