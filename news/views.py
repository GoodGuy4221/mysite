from django.shortcuts import render
from django.http import HttpResponse

from .models import News


def index(request):
    news = News.objects.all()
    context = {
        'title': 'список новостей',
        'news': news,
    }

    return render(request, template_name='news/index.html', context=context)
