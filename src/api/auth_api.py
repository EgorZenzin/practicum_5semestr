import requests

class AuthAPI:
    BASE_URL = "https://restful-booker.herokuapp.com/auth"

    @staticmethod
    def get_token(data):
        response = requests.post(AuthAPI.BASE_URL, json=data)
        return response