from django.test import TestCase

import logging
from django.test import Client
from django.test import TestCase
from burnup.utils import *
from django.urls import reverse
from django.test import Client

# Create your tests here.
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

client = Client(enforce_csrf_checks=True)


class TestCalls(TestCase):
    def test_call_view_without_argument(self):
        test_reverse = reverse('burnup:showburnup')
        response = client.get(test_reverse)
        self.assertEqual(response.status_code, 200)

    def test_call_view_with_comma_velocities_only(self):
        test_reverse = reverse('burnup:showburnup')
        response = client.get(test_reverse, data={'velocities': '1,2,4'})
        self.assertEqual(response.status_code, 200)

    def test_call_view_with_semicolon_velocities_only(self):
        test_reverse = reverse('burnup:showburnup')
        response = client.get(test_reverse, data={'velocities': '1;2:4'})
        self.assertEqual(response.status_code, 200)

    def test_call_view_with_invalid_velocities_only(self):
        test_reverse = reverse('burnup:showburnup')
        response = client.get(test_reverse, data={'velocities': 'w,2,4'})
        self.assertEqual(response.status_code, 200)

    def test_call_view_with_velocities_and_type_XBESTWORST(self):
        test_reverse = reverse('burnup:showburnup')
        response = client.get(test_reverse, data={'velocities': '1,2,4', 'type':2})
        self.assertEqual(response.status_code, 200)
