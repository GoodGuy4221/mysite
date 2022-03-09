from django.urls import path

from .apps import NewsConfig
import news.views as news

app_name = NewsConfig.name

urlpatterns = [
    path('', news.HomeNews.as_view(), name='home'),
    # path('', news.index, name='home'),

    path('category/<int:category_id>/', news.NewsByCategory.as_view(), name='category'),
    path('news/<int:pk>/', news.ViewNews.as_view(), name='view_news'),
    path('news/add-news/', news.CreateNews.as_view(), name='add_news'),

    path('register/', news.register, name='register'),
    path('login/', news.user_login, name='login'),
    path('logout/', news.user_logout, name='logout'),
]
