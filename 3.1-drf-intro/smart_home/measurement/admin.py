from django.contrib import admin


from measurement.models import Measurement, Sensor


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'description']
    ordering = ['id']


#
@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['sensor', 'temperature', 'created_at']
    ordering = ['-created_at']
