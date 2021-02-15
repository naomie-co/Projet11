"""Tests account views"""

from django.test import TestCase
from django.urls import reverse


class LogPagesTestCase(TestCase):

    def test_log_in_page(self):
        """test that login page returns a status code 200"""
        response = self.client.get(reverse('account:log_in'))
        self.assertEqual(response.status_code, 200)

    def test_sign_up_page(self):
        """test that sing_up page returns a status code 200"""
        response = self.client.get(reverse('account:sign_up'))
        self.assertEqual(response.status_code, 200)
    
    def test_log_out_page(self):
        """Test that logout page return a status code 200"""
        response = self.client.get(reverse('account:log_out'))
        self.assertEqual(response.status_code, 200)
    