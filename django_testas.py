from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Word
class AnagramAPITestCase(APITestCase):
    def setUp(self):
        # Create some sample words in the database
        words = ['pale', 'leap', 'plum']
        for word in words:
            Word.objects.create(word=word)
    def test_anagrams_get(self):
        # URL for the get_anagrams endpoint with the word 'pear'
        url = reverse('get_anagrams', args=['pale'])
        response = self.client.get(url)
        # Assert that the request was successful (status code 200)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Assert that the response data contains the correct anagrams
        expected_data = [{
            'word': 'leap'
        }]
        print(response.data)
        self.assertEqual(response.data, expected_data)