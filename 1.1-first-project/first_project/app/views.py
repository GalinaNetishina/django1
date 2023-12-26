import os
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.now().time()
    msg = f'Текущее время: {current_time.hour}:{current_time.minute}'
    return HttpResponse(msg)


def workdir_view(request):
    dir_list = os.listdir()
    res = "<ul>содержимое рабочей директории:"
    for d in dir_list:
        res += f"<li>{d}</li>"
    res += "</ul></div>"
    return HttpResponse(res)
