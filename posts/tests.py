from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Post
from django.contrib.auth.models import User
from rest_framework.test import APIClient


class PostTests(APITestCase):

    def test_view_posts(self):
        url = reverse('posts')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        self.testuser1 = User.objects.create_superuser(
            username='test_user1', password='123456789')
        self.client.login(username=self.testuser1.username,
                          password='123456789')

        data = {"title": "new", "owner": 1,
                 "content": "new"}
        url = reverse('posts')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_update(self):

        client = APIClient()

        self.testuser1 = User.objects.create_user(
            username='test_user1', password='123456789')
        self.testuser2 = User.objects.create_user(
            username='test_user2', password='123456789')
        test_post = Post.objects.create(title='Post Title', content='Post Content',  owner_id=1)

        client.login(username=self.testuser1.username,
                     password='123456789')

        url = reverse(('post_detail'), kwargs={'pk': 1})

        response = client.put(
            url, {
                "title": "New",
                "owner": 1,
                "content": "New",
            }, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

