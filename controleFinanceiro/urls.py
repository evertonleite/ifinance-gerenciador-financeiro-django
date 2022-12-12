from django.contrib import admin
from django.urls import include, path
from main import views

urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('ifinance/', include('main.urls'))
]
