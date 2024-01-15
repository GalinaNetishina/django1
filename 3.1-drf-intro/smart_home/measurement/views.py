# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response

from measurement import serializers
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer


class ListCreateView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = serializers.SensorsSerializer


class SensorUpdateView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = serializers.SensorsSerializer

    def get(self, request, *args, **kwargs):
        self.serializer_class = SensorDetailSerializer
        return super().get(self, request, *args, **kwargs)


class MeasurementCreateView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = serializers.MeasurementSerializer

