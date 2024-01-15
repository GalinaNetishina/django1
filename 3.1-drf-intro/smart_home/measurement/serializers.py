from rest_framework import serializers

from measurement.models import Sensor, Measurement


class MeasurementSerializer(serializers.ModelSerializer):
    temperature = serializers.DecimalField(max_digits=4, decimal_places=1)
    created_at = serializers.CharField(read_only=True)
    photo = serializers.ImageField(read_only=True, allow_null=True)

    class Meta:
        model = Measurement
        exclude = ['id']


class SensorsSerializer(serializers.ModelSerializer):
    description = serializers.CharField(allow_null=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']