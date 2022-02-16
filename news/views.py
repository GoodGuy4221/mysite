from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    print(dir(request))
    return HttpResponse('Hi!')


def test(request):
    return HttpResponse('<h1>Testing page!</h1>')
