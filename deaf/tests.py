from PIL import Image
import tempfile

from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from account.models import User
from deaf.models import CategoriesOfTheDeaf, Sentence


class CategoryOfDeafTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='123')
        self.token = Token.objects.get(user__username='tester')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        image = Image.new('RGB', (100, 100))

        self.tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(self.tmp_file)
        self.tmp_file.seek(0)

        self.category = CategoriesOfTheDeaf.objects.create(title='test', url_title='test_url')

    def test_category_create(self):
        data = {
            "title": "Test Category",
            "icon": self.tmp_file,
            "url_title": "test_url"
        }
        response = self.client.post(reverse('category_of_the_deaf-list'), data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_category_list(self):
        response = self.client.get(reverse('category_of_the_deaf-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_category_detail(self):
        response = self.client.get(reverse('category_of_the_deaf-detail', args=(self.category.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_category_edit(self):
        data = {
            "title": "Test Category-update",
            "icon": self.tmp_file,
            "url_title": "test_url-update"
        }
        response = self.client.put(reverse('category_of_the_deaf-detail', args=(self.category.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_category_delete(self):
        response = self.client.delete(reverse('category_of_the_deaf-detail', args=(self.category.id,)))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class SentenceTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='123')
        self.token = Token.objects.get(user__username='tester')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.sentence = Sentence.objects.create(title="test", video_url="test_url")

    def test_sentence_create(self):
        data = {
            "title": "test",
            "video_url": "test_url"
        }
        response = self.client.post(reverse('sentence-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_sentence_list(self):
        response = self.client.get(reverse('sentence-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_sentence_detail(self):
        response = self.client.get(reverse('sentence-detail', args=(self.sentence.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Sentence.objects.count(), 1)

    def test_sentence_edit(self):
        data = {
            "title": "test-edit",
            "video_url": "test_url-edit"
        }
        response = self.client.put(reverse('sentence-detail', args=(self.sentence.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_sentence_delete(self):
        response = self.client.delete(reverse('sentence-detail', args=(self.sentence.id,)))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class SentenceCategoryTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='123')
        self.token = Token.objects.get(user__username='tester')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.category = CategoriesOfTheDeaf.objects.create(title='test', url_title='test_url')

    def test_sentence_category_list(self):
        response = self.client.get(reverse('category-list', args=(self.category.title,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
