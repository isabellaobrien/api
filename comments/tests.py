from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Comment
from django.contrib.auth.models import User
from rest_framework.test import APIClient


class CommentTests(APITestCase):

    def test_view_comments(self):
        url = reverse('comments')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
