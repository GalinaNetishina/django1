# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from measurement import serializers
from measurement.models import Sensor


class ListCreateView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = serializers.SensorsSerializer
    
    def post(self, request):
        serializer = serializers.SensorsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if not pk:
            return Response({'error': 'method PUT not allowed'})
        try:
            instance = Sensor.objects.get(pk=pk)
        except:
            return Response({'error': f'object with pk={pk} does not exist'})

        serializer = serializers.SensorsSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})
    

class SensorDetailView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = serializers.SensorDetailSerializer
