from django.core.urlresolvers import reverse
from django.core.urlresolvers import resolve
import unittest


class Urls(unittest.TestCase):

    def test_urls(self):
        url = reverse('login')
        self.assertEqual(url, '/login/')

        url = reverse('dashboard')
        self.assertEqual(url, '/Dashboard')

        url = reverse('op_area_detail', args=['opArea'])
        self.assertEqual(url, '/OpAreaDetail/opArea/')




