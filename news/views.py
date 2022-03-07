from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from .models import News, Category
from .forms import NewsForm
from .utils import MyMixin


class HomeNews(MyMixin, ListView):
    model = News
    extra_context = {
        'title': 'список новостей',
    }
    template_name = 'news/index.html'
    context_object_name = 'news'
    mixin_prop = 'hello world'
    paginate_by = 5

    # queryset = News.objects.select_related('category').filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mixin_prop'] = self.get_prop()
        context['title'] = self.get_upper('Главная страница')
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


# def index(request):
#     news = News.objects.all()
#     paginator = Paginator(news, 5)
#     page_num = request.GET.get('page', default=1)
#     page_obj = paginator.get_page(page_num)
#     context = {
#         'title': 'список новостей',
#         'page_obj': page_obj,
#     }
#
#     return render(request, template_name='news/index.html', context=context)


class NewsByCategory(MyMixin, ListView):
    model = News
    template_name = 'news/category.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 5

    def get_queryset(self):
        queryset = News.objects.filter(
            category=self.kwargs['category_id'],
            is_published=True,
        ).select_related('category')
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = Category.objects.get(pk=self.kwargs['category_id']).title
        return context


# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#
#     context = {
#         'news': news,
#         'category': category,
#     }
#
#     return render(request=request, template_name='news/category.html', context=context)


class ViewNews(DetailView):
    model = News
    # pk_url_kwarg = 'news_id'
    # template_name = 'news/news_detail.html'
    context_object_name = 'news_item'


# def view_news(request, news_id: int):
#     # news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News, pk=news_id)
#     context = {
#         'news_item': news_item,
#     }
#     return render(request=request, template_name='news/news_detail.html', context=context)


class CreateNews(LoginRequiredMixin, CreateView):
    # login_url = 'news:home'
    # login_url = reverse_lazy('news:home')
    raise_exception = True

    form_class = NewsForm
    template_name = 'news/add_news.html'
    # success_url = reverse_lazy('news:home')

# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST, request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             # news = News.objects.create(**form.cleaned_data)
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#
#     context = {
#         'form': form,
#     }
#
#     return render(request=request, template_name='news/add_news.html', context=context)
