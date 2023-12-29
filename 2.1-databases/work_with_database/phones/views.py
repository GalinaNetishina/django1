from django.shortcuts import render, redirect

from phones.management.commands.import_phones import Command
from phones.models import Phone


def index(request):
    Command.handle()
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones_obj = Phone.objects.all()
    context = {'phones': phones_obj}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)
