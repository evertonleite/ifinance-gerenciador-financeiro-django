from django.test import TestCase, Client
from django.urls import reverse

from django.contrib.auth.models import User
from main.models import Categorias, Despesas, Receitas


class TestViews(TestCase):
    def test_get_url():
        pass
