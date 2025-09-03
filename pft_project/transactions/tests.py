from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Category

class PermissionsTest(APITestCase):
    def setUp(self):
        # Create two distinct users
        self.user1 = User.objects.create_user(username='user1', password='password123')
        self.user2 = User.objects.create_user(username='user2', password='password123')

        # Create a category that belongs only to user1
        self.category_user1 = Category.objects.create(name='User1 Category', user=self.user1)

    def get_jwt_token(self, username, password):
        url = '/api/auth/token/'
        response = self.client.post(url, {"username": username, "password": password}, format='json')
        return response.data['access']

    def test_user_cannot_see_another_users_data(self):
        """
        Ensure that a user cannot list or retrieve categories owned by another user.
        """
        # Obtain JWT token for user2
        token = self.get_jwt_token('user2', 'password123')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        # Attempt to access the list endpoint. It should only show user2's categories (which is none).
        response_list = self.client.get('/api/categories/')
        self.assertEqual(response_list.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_list.data), 0) # Should be an empty list

        # Attempt to directly access user1's category by its ID
        response_detail = self.client.get(f'/api/categories/{self.category_user1.id}/')
        # The correct behavior is to deny access
        self.assertEqual(response_detail.status_code, status.HTTP_404_NOT_FOUND)
