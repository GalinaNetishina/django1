from django.http import HttpResponse
from django.shortcuts import render, redirect

from phones.models import Phone


# Create your views here.
def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    SORT_MAP = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price',
        }
    phones = Phone.objects.all()
    sort = request.GET.get('sort')
    if sort:
        phones = phones.order_by(SORT_MAP[sort])
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    return render(request, template, context={'phone': phone})
