import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse


# initialize the APIClient app
client = Client()


class CreateNewCustomerTest(TestCase):
    """ Test module for inserting a new customer """

    def setUp(self):
        self.valid_payload = {
            'first_name': 'Jack',
            'last_name': 'Mech',
            'dob': '25-06-1991'
        }
        self.invalid_payload = {
            'first_name': 'Jack',
            'last_name': 'Mech',
            'dob': '25-06-199'
        }

    def test_create_valid_customer(self):
        response = client.post(
            reverse('create_customer'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_customer(self):
        response = client.post(
            reverse('create_customer'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)