import mysql.connector
from config import USER, PASSWORD, HOST


class DbConnectionError(Exception):
    pass


# Connect to mySQL database
def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx


# Take schedule and present in readable format for user
def _map_values(schedule):
    mapped = []
    for item in schedule:
        mapped.append({
            'name': item[0],
            '9-12': 'Not Available' if item[1] else 'Available',
            '13-18': 'Not Available' if item[2] else 'Available',
            '19-23': 'Not Available' if item[3] else 'Available',
        })
    return mapped


# Fetch data from database and present in readable format, handle exceptions before closing connection
def view_booking_availability(date):
    availability = []
    try:
        db_name = 'excursions'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = f"""
        SELECT tour_guide, `9-12`, `13-18`, `19-23`
        FROM excursion_bookings
        WHERE booking_date = '{date}';
        """

        cur.execute(query)

        result = cur.fetchall()
        print(result)

        availability = _map_values(result)
    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    return availability


# Update database to add new booking
def add_booking(date, tour_guide, time, customer):
    try:
        db_name = 'excursions'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = f"""
        UPDATE excursion_bookings
        SET `{time}` = 1,
            `{time}_bookingid` = '{customer}'
        WHERE tour_guide = '{tour_guide}'
          AND booking_date = '{date}'
        """

        cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


# Update exisiting booking in database
def edit_booking(date, tour_guide, time, customer):
    try:
        db_name = 'excursions'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = f"""
        UPDATE excursion_bookings
        SET `{time}` = 1,
            `{time}_bookingid` = '{customer}'
        WHERE tour_guide = '{tour_guide}'
          AND booking_date = '{date}'
        """

        cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")
