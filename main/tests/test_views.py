from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from main.models import Categorias


class TestViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            first_name="teste", email="teste@gmail.com", username="teste"
        )
        self.user.set_password("12345")
        self.user.save()

        self.client = Client()
        self.client.login(username="teste", password="12345")

    def test_home_logged(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_despesas_logged(self):
        response = self.client.get(reverse("despesa"))
        self.assertEqual(response.status_code, 200)

    def test_receita_logged(self):
        response = self.client.get(reverse("receita"))
        self.assertEqual(response.status_code, 200)

    def test_create_categoria_logged(self):
        category = {"name": "teste", "user_id": self.user}
        response = self.client.post(
            reverse("create_category"),
            category,
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
