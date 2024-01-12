from django.urls import path

from measurement.views import ListCreateView, SensorDetailView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    
    path('sensors/', ListCreateView.as_view()),
    path('sensors/<pk>/', ListCreateView.as_view()),
    #path('sensors/<pk>/', SensorDetailView.as_view()),
    #path('measurements/', get_measurements)
]
