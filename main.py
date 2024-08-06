import json
import requests


# Get available dates and display in JSON
def get_availability_by_date(date):
    result = requests.get(f'http://localhost:5001/availability/{date}')
    return result.json()


# Print table with tour guides and their available time slots for each date
def display_availability(records):
    print("{:<15} {:<15} {:<15} {:<15} ".format(
        'NAME', '9-12', '13-18', '19-23'))
    print('-' * 105)

    for item in records:
        print("{:<15} {:<15} {:<15} {:<15} ".format(
            item['name'], item['9-12'], item['13-18'], item['19-23']
        ))


# Create booking dictionary and add booking to database
def add_booking(date, tour_guide, time, cust):
    booking = {
        "date": date,
        "tour_guide": tour_guide,
        "time": time,
        "customer": cust,
    }
    response = requests.put(
        'http://localhost:5001/booking',
        headers={'content-type': 'application/json'},
        data=json.dumps(booking)
    )


# Update existing booking with new details
def edit_booking(date, tour_guide, time, cust):
    booking = {
        "date": date,
        "tour_guide": tour_guide,
        "time": time,
        "customer": cust,
    }
    response = requests.put(
        'http://localhost:5001/booking/edit',
        headers={'content-type': 'application/json'},
        data=json.dumps(booking)
    )


# Booking process for customer
def run():
    print('############################')
    print('Hello, let us help you book your excursion')
    print('############################')
    print()
    print('############################')
    print('We currently have excursions during the week between 2024-07-01 and 2024-07-07')
    print('############################')
    print()
    date = input('What date you would like to check availability for (YYYY-MM-DD): ')
    print()
    slots = get_availability_by_date(date)
    # print(slots)
    print('####### AVAILABILITY #######')
    print()
    display_availability(slots)
    print()
    booking_choice = input('Would you like to book an excursion or edit booking name? (book/edit)  ')
    book = booking_choice == 'book'
    edit = booking_choice == 'edit'

    if book:
        cust = input('Enter your name: ')
        tour_guide = input('Choose your guide (Joe, Amy): ')
        time = input('Choose time based on availability. Our slots are 9-12, 13-18 and 19-23: ')
        add_booking(date, tour_guide, time, cust)
        print("Booking successful")
        print()
        slots = get_availability_by_date(date)
        display_availability(slots)
        print()
        print('Enjoy your excursion!')
    elif edit:
        print('Please enter the details of your booking')
        tour_guide = input('Who was your guide? (Joe, Amy): ')
        date = input('What date did you want to book for (YYYY-MM-DD)? ')
        time = input('Which time slot is the booking for? ')
        print('Please enter the updated name you would like on your booking: ')
        cust = input('Enter your name: ')
        edit_booking(date, tour_guide, time, cust)
        print("Booking name edited")
        print()
        slots = get_availability_by_date(date)
        display_availability(slots)
        print()
        print('Enjoy your excursion!')


if __name__ == '__main__':
    run()
