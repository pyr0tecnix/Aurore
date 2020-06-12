from datetime import datetime
from django.test import TestCase
from django.core.exceptions import ObjectDoesNotExist
from api.models import *


class AlarmCreateTest(TestCase):
    """ Test Alarm Model """

    def setUp(self):
        self.alarm = Alarm.objects.create(name = 'Test', hour = datetime.now().time(), duration = 1, days = '1,2,3', status = True)

    def test_alarm_get(self):
        alarm = Alarm.objects.get(name='Test')
        self.assertEqual(str(alarm), str(self.alarm))

    def test_alarm_update(self):
        alarm = Alarm.objects.get(name='Test')
        alarm.name = 'Updated'
        alarm.save()

        alarmUpdated = Alarm.objects.get(name = 'Updated')
        print(alarmUpdated)
        self.assertEqual(str(alarm), str(alarmUpdated))

    def test_alarm_delete(self):
        Alarm.objects.get(name = 'Test').delete()
        self.assertRaises(ObjectDoesNotExist, Alarm.objects.get, name = 'Test')

class ColorTest(TestCase):
    """ Test Color Model """

    def setUp(self):
        self.color = Color.objects.create(color = '#AABBCC')

    def test_color_get(self):
        color = Color.objects.get(color='#AABBCC')
        self.assertEqual(str(color), str(self.color))

    def test_color_update(self):
        color = Color.objects.get(color='#AABBCC')
        color.color = '#00FF00'
        color.save()

        colorUpdated = Color.objects.get(color = '#00FF00')
        print(colorUpdated)
        self.assertEqual(str(color), str(colorUpdated))

    def test_color_delete(self):
        Color.objects.get(color = '#AABBCC').delete()
        self.assertRaises(ObjectDoesNotExist, Color.objects.get, color = '#AABBCC')


