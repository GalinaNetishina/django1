from django.http import HttpResponse
from django.shortcuts import render, redirect

from phones.models import Phone


# Create your views here.
def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort')
    template = 'catalog.html'
    match sort:
        case 'name':
            phones = Phone.objects.order_by('name')
        case 'max_price':
            phones = Phone.objects.order_by('-price')
        case 'min_price':
            phones = Phone.objects.order_by('price')
        case _:
            phones = Phone.objects.all()

    return render(request, template, {'phones': phones})


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    return render(request, template, context={'phone': phone})
