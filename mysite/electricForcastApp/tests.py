from django.test import TestCase

from .models import Entry

# Create your tests here.
class ProjectTests(TestCase):

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

from django.contrib.auth import get_user_model


class HomePageTests(TestCase):

    """Test whether our blog entries show up on the homepage"""

    def setUp(self):
        self.user = get_user_model().objects.create(username='some_user')

    def test_login_page(self):
        response = self.client.get('/admin')
        self.assertEqual(response.status_code, 200)

    def test_dashboard_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_opArea_page(self):
        response = self.client.get('/OpArea/')
