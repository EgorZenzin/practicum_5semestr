import pytest
from src.api.booking_api import BookingAPI
from src.api.auth_api import AuthAPI

class TestCreateBooking:

    def test_create_booking(self):
        auth_data = {
            "username": "admin",
            "password": "password123"
        }
        token_response = AuthAPI.get_token(auth_data)
        assert token_response.status_code == 200
        token = token_response.json()["token"]

        data = {
            "firstname": "Egor",
            "lastname": "Zenzin",
            "totalprice": 150,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2024-01-01",
                "checkout": "2024-01-15"
            },
            "additionalneeds": "Breakfast"
        }

        response = BookingAPI.create_booking(data)

        assert response.status_code == 200
        response_data = response.json()
        assert response_data['bookingid'] is not None
        assert response_data['booking']['firstname'] == "Egor"

        booking_id = response_data['bookingid']
        delete_response = BookingAPI.delete_booking(booking_id, token)  
        assert delete_response.status_code == 403  