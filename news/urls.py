from django.urls import path

from .apps import NewsConfig
import news.views as news

app_name = NewsConfig.name

urlpatterns = [
    path('', news.HomeNews.as_view(), name='home'),
    path('category/<int:category_id>/', news.NewsByCategory.as_view(), name='category'),
    path('news/<int:news_id>/', news.view_news, name='view_news'),
    path('news/add-news/', news.add_news, name='add_news'),
]
