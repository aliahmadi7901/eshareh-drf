import tempfile

from PIL import Image
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from account.models import User
from word.models import CategorizeWord, Word


class CategoryWordTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='123')
        self.token = Token.objects.get(user__username='tester')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        image = Image.new('RGB', (100, 100))

        self.tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(self.tmp_file)
        self.tmp_file.seek(0)

        self.category = CategorizeWord.objects.create(title="test", url_title='test')

    def test_category_creation(self):
        data = {
            "title": "Test title",
            "icon": self.tmp_file,
            "url_title": "Test title",
        }
        response = self.client.post(reverse('categorize-list'), data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_category_list(self):
        response = self.client.get(reverse('categorize-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_category_idn(self):
        response = self.client.get(reverse('categorize-detail', args=(self.category.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_category_edit(self):
        data = {
            "title": "Test title--edit",
            "icon": self.tmp_file,
            "url_title": "Test title--edit",
        }
        response = self.client.put(reverse('categorize-detail', args=(self.category.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_category_delete(self):
        response = self.client.delete(reverse('categorize-detail', args=(self.category.id,)))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class WordTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='123')
        self.token = Token.objects.get(user__username='tester')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        image = Image.new('RGB', (100, 100))

        self.tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(self.tmp_file)
        self.tmp_file.seek(0)

        self.category = CategorizeWord.objects.create(title="test", url_title='test')
        self.word = Word.objects.create(title="test", pronunciation_of_the_word="test", video_url="test_url")

    def test_word_create(self):
        data = {
            "title": "test",
            "pronunciation_of_the_word": "test",
            "image": self.tmp_file,
            "video_url": "test_url",
            "categorize_word": self.category
        }
        response = self.client.post(reverse('words-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def tset_word_list(self):
        response = self.client.get(reverse('words-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_word_idn(self):
        response = self.client.get(reverse('words-detail', args=(self.word.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_word_edit(self):
        data = {
            "title": "test--edit",
            "pronunciation_of_the_word": "test--edit",
            "image": self.tmp_file,
            "video_url": "test_url--edit",
            "categorize_word": self.category
        }
        response = self.client.put(reverse('words-detail', args=(self.word.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_word_delete(self):
        response = self.client.delete(reverse('words-detail', args=(self.word.id,)))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class CreateSentenceTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='123')
        self.token = Token.objects.get(user__username='tester')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.word = Word.objects.create(title="test", pronunciation_of_the_word="test", video_url="test_url")

    def test_create_sentence(self):
        response = self.client.get(reverse('create_sentence', args=(self.word.title,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
