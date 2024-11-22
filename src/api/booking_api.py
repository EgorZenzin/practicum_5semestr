import requests

class BookingAPI:
    BASE_URL = "https://restful-booker.herokuapp.com/booking"

    @staticmethod
    def create_booking(data):
        response = requests.post(BookingAPI.BASE_URL, json=data)
        return response

    @staticmethod
    def update_booking(booking_id, data):
        response = requests.put(f"{BookingAPI.BASE_URL}/{booking_id}", json=data)
        return response

    @staticmethod
    def delete_booking(booking_id, token):
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.delete(f"{BookingAPI.BASE_URL}/{booking_id}", headers=headers)
        return response

    @staticmethod
    def get_booking(booking_id):
        response = requests.get(f"{BookingAPI.BASE_URL}/{booking_id}")
        return response