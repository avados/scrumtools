from django.test import TestCase

import logging
from django.test import Client
from django.test import TestCase
from burnup.utils import *
from django.urls import reverse
from django.test import Client
from hamcrest import *

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
        response = client.get(test_reverse, data={'velocities': '1,2,4', 'type': 2})
        self.assertEqual(response.status_code, 200)

    def test_extend_scope_for_chartjs_with_unique_int_value(self):
        scope = 6
        ext_scope = get_extended_scope(scope, 5)
        assert_that(ext_scope, equal_to([6, 6, 6, 6, 6]))

    def test_extend_scope_for_chartjs_with_unique_str_value(self):
        scope = "6"
        ext_scope = get_extended_scope(scope, 5)
        assert_that(ext_scope, equal_to([6, 6, 6, 6, 6]))

    def test_extend_scope_for_chartjs_with_list_of_several_int_values(self):
        scope = [6,10,12]
        ext_scope = get_extended_scope(scope, 5)
        assert_that(ext_scope, equal_to([6, 10, 12, 12, 12]))

    def test_extend_scope_for_chartjs_with_str_values(self):
        scope = "6,10,12"
        ext_scope = get_extended_scope(scope, 5)
        assert_that(ext_scope, equal_to([6, 10, 12, 12, 12]))

        #todo test views/templates see https://test-driven-django-development.readthedocs.io/en/latest/03-views.html