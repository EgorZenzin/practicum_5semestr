import pytest
from src.api.auth_api import AuthAPI

class TestGetToken:

    def test_get_token(self):
        data = {
            "username": "admin",
            "password": "password123"
        }

        response = AuthAPI.get_token(data)

        assert response.status_code == 200
        response_data = response.json()
        assert "token" in response_data
        assert len(response_data["token"]) > 0  