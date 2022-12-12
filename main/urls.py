from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('despesa/', views.despesa, name='despesa'),
    path('receita/', views.receita, name='receita'),
    path('logout/', views.logout, name='logout'),
]
