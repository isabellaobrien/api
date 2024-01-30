from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Profile
from django.contrib.auth.models import User
from rest_framework.test import APIClient


class PostTests(APITestCase):

    def test_view_posts(self):
        url = reverse('profiles')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    