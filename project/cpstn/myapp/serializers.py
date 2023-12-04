from rest_framework import serializers
from .models import Test,Schedule,Disease

class TestSerializer(serializers.ModelSerializer):
    class TestMeta:
        model = Test
        fields = '__all__'
        
class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('scheduleId', 'event', 'temp','year', 'month', 'day', 'time', 'detail')


class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = ['name', 'detail']