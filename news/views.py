from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect

from .models import News, Category
from .forms import NewsForm


def index(request):
    news = News.objects.all()
    context = {
        'title': 'список новостей',
        'news': news,
    }

    return render(request, template_name='news/index.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)

    context = {
        'news': news,
        'category': category,
    }

    return render(request=request, template_name='news/category.html', context=context)


def view_news(request, news_id: int):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    context = {
        'news_item': news_item,
    }
    return render(request=request, template_name='news/view_news.html', context=context)


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            # news = News.objects.create(**form.cleaned_data)
            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()

    context = {
        'form': form,
    }

    return render(request=request, template_name='news/add_news.html', context=context)
