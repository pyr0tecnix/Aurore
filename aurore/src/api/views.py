from django.shortcuts import render

from rest_framework import serializers, viewsets

from . import models


class AlarmSerializer(serializers.Serializer):
    name = serializers.CharField()

class Alarms(viewsets.ModelViewSet):
    serializer_class = AlarmSerializer
    queryset = models.Alarm.objects.all()


class ColorSerializer(serializers.Serializer):
    color = serializers.CharField()

class Colors(viewsets.ModelViewSet):
    serializer_class = ColorSerializer
    queryset = models.Color.objects.all()