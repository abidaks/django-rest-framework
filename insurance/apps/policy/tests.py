import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse


# initialize the APIClient app
client = Client()


class CreateNewPolicyTest(TestCase):
    """ Test module for inserting a new Policy """

    def setUp(self):
        self.valid_payload = {
            'type': 'personal-accident',
            'premium': 200,
            'cover': 200000,
            'customer_id': 1
        }
        self.invalid_payload = {
            'type': 'personal-accident',
            'premium': 200,
            'cover': 200000,
            'customer_id': 55
        }
        
        self.cust_data = {
            'first_name': 'Jack',
            'last_name': 'Mech',
            'dob': '25-06-1991'
        }

    def test_create_valid_policy(self):
        cust_response = client.post(
            reverse('create_customer'),
            data=json.dumps(self.cust_data),
            content_type='application/json'
        )
        
        response = client.post(
            reverse('create_policy'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_policy(self):
        response = client.post(
            reverse('create_policy'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)