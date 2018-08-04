from django.shortcuts import render


def index(request):
    return render(request, 'sitepages/index.html')


def article1(request):
    return render(request, 'sitepages/article1.html')


def article2(request):
    return render(request, 'sitepages/article2.html')