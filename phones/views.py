from django.shortcuts import render, redirect
from phones.models import Phone
from pprint import pprint

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones = Phone.objects.filter(slug=slug)
    context = {'phone': phones}
    return render(request, template, context)
