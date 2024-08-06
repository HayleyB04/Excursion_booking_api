from flask import Flask, jsonify, request
from db_utils import view_booking_availability, add_booking, edit_booking

app = Flask(__name__)


# Handle get requests
@app.route('/availability/<date>')
def get_bookings(date):
    print(date)
    res = view_booking_availability(date)
    return jsonify(res)


# Handle put requests, call add_booking function
@app.route('/booking', methods=['PUT'])
def book_excursion():
    booking = request.get_json()
    add_booking(
        date=booking['date'],
        tour_guide=booking['tour_guide'],
        time=booking['time'],
        customer=booking['customer'],
    )


# Handle put requests, call edit_booking function
@app.route('/booking/edit', methods=['PUT'])
def edit_excursion():
    booking = request.get_json()
    edit_booking(
        date=booking['date'],
        tour_guide=booking['tour_guide'],
        time=booking['time'],
        customer=booking['customer']
    )


# Run flask app in debug mode
if __name__ == '__main__':
    app.run(debug=True, port=5001)
