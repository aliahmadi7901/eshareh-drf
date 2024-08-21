from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from account.models import User


class RegisterTestCase(APITestCase):
    def test_register(self):
        data = {
            "phone_number": "09127632162",
            "username": "ali",
            "password": "123",
            "confirm_password": "123"
        }
        response = self.client.post(reverse('register_page'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LoginLogoutTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="ali", password='123')

    def test_login(self):
        data = {
            "username": "ali",
            "password": "123"
        }
        response = self.client.post(reverse('login_page'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout(self):
        self.token = Token.objects.get(user__username="ali")
        self.client.credentials(HTTP_AUTHORIZATION='Token' + self.token.key)
        response = self.client.post(reverse('logout_page'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

