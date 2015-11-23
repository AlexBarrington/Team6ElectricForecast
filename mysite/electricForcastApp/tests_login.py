from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test.client import Client
import unittest

from django.http import HttpResponsePermanentRedirect
from django.test.client import Client

# Create your tests here.

from django.contrib.auth import get_user_model
from electricForcastApp.models import MyUser
from electricForcastApp.models import MyUserManager


class LoginTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.user = MyUser.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

    def testLogin(self):
        self.client.login(username='lennon@thebeatles.com', password='johnpassword')
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def testDashboardLoggedIn(self):
        self.client.login(username='lennon@thebeatles.com', password='johnpassword')
        loginResponse = self.client.get(reverse('login'))
        self.assertEqual(loginResponse.status_code, 200)
        response = self.client.get('dashboard')
        self.assertEqual(response.status_code, 200)

    def testOpAreaLoggedIn(self):
        self.client.login(username='lennon@thebeatles.com', password='johnpassword')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        self.user.delete()



