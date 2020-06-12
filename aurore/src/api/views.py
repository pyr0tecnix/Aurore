from django.shortcuts import render

from rest_framework import serializers, viewsets

from . import models


class AlarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Alarm
        fields = '__all__'


class Alarms(viewsets.ModelViewSet):
    serializer_class = AlarmSerializer
    queryset = models.Alarm.objects.all()

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Color
        fields = '__all__'

class Colors(viewsets.ModelViewSet):
    serializer_class = ColorSerializer
    queryset = models.Color.objects.all()