from django.test import TestCase
from rest_framework.test import APIRequestFactory
from .models import FizzBuzz
from .views import fizzBuzz


class TestViews(TestCase):
    def test_get_fizzbuzz(self):
        factory = APIRequestFactory()
        request = factory.get('/fizzbuzz/')
        response = fizzBuzz(request)
        
        self.assertEqual(200, response.status_code)
    
    def test_create_fizzbuzz(self):
        factory = APIRequestFactory()
        request = factory.post('/fizzbuzz/', {"message": "create test"})
        response = fizzBuzz(request)

        self.assertEqual(200, response.status_code)
        self.assertEqual('create test', response.data["message"])

    def test_single_fizzbuzz(self):
        factory = APIRequestFactory()

        request = factory.post('/fizzbuzz/', {"message": "first"})
        response = fizzBuzz(request)
        request = factory.post('/fizzbuzz/', {"message": "second"})
        response = fizzBuzz(request)
        request = factory.post('/fizzbuzz/', {"message": "third"})
        response = fizzBuzz(request)

        request = factory.get('/fizzbuzz/1')
        response = fizzBuzz(request)

        print(response.data)

        self.assertEqual(200, response.status_code)
        self.assertEqual('second', response.data[1]["message"])

    
# Create your tests here.
