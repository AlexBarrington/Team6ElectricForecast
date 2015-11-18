from django.test import *
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test.client import Client
import unittest

from django.http import HttpResponsePermanentRedirect
from django.test.client import Client

# Create your tests here.


class UrlsTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def urls(self):
        url = reverse('archive-summary', args=[1988])
        #assertEqual(url, '/archive/')

        url = reverse('archive-summary', args=[1988])
        #assertEqual(url, '/archive-summary/1988/')


