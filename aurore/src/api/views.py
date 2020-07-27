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


class ContentObjectRelatedField(serializers.RelatedField):
    """
    A custom field to use for the `content_object` generic relationship.
    """

    def to_representation(self, value):
        """
        Serialize tagged objects to a simple textual representation.
        """
        print(value)
        if isinstance(value, models.Alarm):
            return value.name
        elif isinstance(value, models.Color):
            return value.color
        else:
            raise Exception('Unexpected type of tagged object')

class RunningSerializer(serializers.ModelSerializer):
    # running_content_object = ContentObjectRelatedField()
    class Meta:
        model = models.Running
        fields = ('content_type', 'object_id', 'running_content_object')

class Running(viewsets.ModelViewSet):
    serializer_class = RunningSerializer
    queryset = models.Running.objects.all()