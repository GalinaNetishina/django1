import csv
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    all_stations = []
    with open('pagination/stations_data.csv', encoding='utf-8') as f:
        f.readline()
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            station = {
                "Name": row["Наименование"].split(',')[0],
                "Street": row["Наименование"].split(',')[1],
                "District": row["Район"]
            }
            all_stations.append(station)

    paginator = Paginator(all_stations, 10)
    page = paginator.get_page(page_number)
    context = {
         'bus_stations': page,
         'page': page,
    }
    return render(request, 'stations/index.html', context)
