from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('despesa/', views.despesa, name='despesa'),
    path('despesa/criar/', views.create_despesa, name='create_despesa'),
    path('despesa/apagar/<int:id>', views.delete_despesa, name='delete_despesa'),
    path('receita/', views.receita, name='receita'),
    path('receita/criar/', views.create_receita, name='create_receita'),
    path('receita/apagar/<int:id>', views.delete_receita, name='delete_receita'),
    path('categoria/', views.create_category, name='create_category'),
    path('categoria/apagar/<int:id>', views.delete_categoria, name='delete_category'),
    path('logout/', views.logout, name='logout'),
]
