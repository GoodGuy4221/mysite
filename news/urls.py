from django.urls import path

from .apps import NewsConfig
from .views import index, get_category

app_name = NewsConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category_id>/', get_category, name='get_category'),
]
