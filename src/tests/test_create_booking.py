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

        get_response = BookingAPI.get_booking(booking_id)
        assert get_response.status_code == 200
        get_response_data = get_response.json()
        assert get_response_data['firstname'] == "Egor"
        assert get_response_data['lastname'] == "Zenzin"
        assert get_response_data['totalprice'] == 150
        assert get_response_data['depositpaid'] is True
        assert get_response_data['bookingdates']['checkin'] == "2024-01-01"
        assert get_response_data['bookingdates']['checkout'] == "2024-01-15"
        assert get_response_data['additionalneeds'] == "Breakfast"

        delete_response = BookingAPI.delete_booking(booking_id, token)  
        assert delete_response.status_code == 403  