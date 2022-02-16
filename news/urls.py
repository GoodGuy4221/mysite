from django.urls import path

from .apps import NewsConfig
from .views import index

app_name = NewsConfig.name

urlpatterns = [
    path('', index, name='index'),
]
