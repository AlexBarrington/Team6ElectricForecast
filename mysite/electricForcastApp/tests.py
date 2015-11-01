from django.test import TestCase


# Create your tests here.


from django.contrib.auth import get_user_model


class HomePageTests(TestCase):

    """Test whether our blog entries show up on the homepage"""

    def setUp(self):
        self.user = get_user_model().objects.create(username='britt.ahlgrim@gmail.com')
        # self.password = get_user_model().objects.create(password='password')



    def test_login_page(self):
        response = self.client.get('/admin/login/?next=/admin/')
        self.assertEqual(response.status_code, 200)

    def test_dashboard_page(self):
        response = self.client.get('/Home/')
        self.assertEqual(response.status_code, 200)


    def test_opArea_page(self):
        response = self.client.get('/OpArea/')
        self.assertEqual(response.status_code, 200)



