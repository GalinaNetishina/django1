from django.conf.urls.static import static
from django.urls import path

from measurement.views import ListCreateView, SensorUpdateView, MeasurementCreateView
from smart_home import settings

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    
    path('sensors/', ListCreateView.as_view()),# ListCreateAPIView
    path('sensors/<pk>/', SensorUpdateView.as_view()), # RetrieveUpdateAPIView
    path('measurements/', MeasurementCreateView.as_view()) # CreateAPIView
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
