from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort', "no")

    match sort:
        case 'no':
            phones = Phone.objects.all()
        case 'name':
            phones = Phone.objects.all().order_by('name')
        case 'min_price':
            phones = Phone.objects.all().order_by('price')
        case 'max_price':
            phones = Phone.objects.all().order_by('price').reverse()
        case _:
            phones = Phone.objects.all()

    template = 'catalog.html'

    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones = Phone.objects.get(slug=slug)
    context = {'phone': phones}
    return render(request, template, context)
