import csv
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    all_stations = []
    with open(BUS_STATION_CSV, encoding='utf-8') as f:
        f.readline()
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            station = {
                "Name": row["Название остановки"],
                "Street": row["Описание места расположения объекта"],
                "District": row["Район"].replace('район', '').strip()
            }
            all_stations.append(station)

    paginator = Paginator(all_stations, 10)
    page = paginator.get_page(page_number)
    context = {
         'bus_stations': page,
         'page': page,
    }
    return render(request, 'stations/index.html', context)
