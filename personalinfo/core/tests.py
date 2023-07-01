from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from core.models import Profile

# Create your tests here.

USER_URL = reverse('Create-user')

def create_user(**params):
    payload ={
            'username':'testuser',
            'email':'testuser@gmail.com',
            'first_name':'test',
            'last_name':'user1',
            'password':'user@123'
        }
    payload.update(params)
    user = get_user_model().objects.create(**payload)
    user.save()
    return user

class APITesting(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.payload ={
            'username':'testuser',
            'email':'testuser@gmail.com',
            'first_name':'test',
            'last_name':'user1',
            'password':'user@123'
        }


    def test_create_user(self):
        res = self.client.post(USER_URL, self.payload, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['email'], self.payload['email'])

    def test_profile_create(self):
        profile_data ={
            'address':'2 Adejumo street, ilupeju',
            'phone':'090123456'
        }

        user = create_user()
        profile = Profile.objects.create(user=user, **profile_data)
        self.assertEqual(str(profile), user.first_name)