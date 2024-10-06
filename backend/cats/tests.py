"""Docsting."""
from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient


class CatsAPITestCase(TestCase):
    """Docsting."""

    def setUp(self):
        """Docsting."""
        User = get_user_model()  # noqa: N806
        self.user = User.objects.create_user(username='auth_user')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_list_exists(self):
        """Docsting."""
        """Проверка доступности списка задач."""
        response = self.client.get('/api/cats/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
