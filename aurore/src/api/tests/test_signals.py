from django.test import TestCase
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from api.models import *

class ResetDefaultColor(TestCase):
    """ Test reset default color """

    def setUp(self):
        Color.objects.create(color="#FFFFFF", default=True)

    def test_reset_from_create(self):
        defaultColor = Color.objects.create(color="#FFFF00", default=True)

        oldDefaultColor = Color.objects.get(color="#FFFFFF")

        self.assertTrue(defaultColor.default)
        self.assertFalse(oldDefaultColor.default)


    def test_reset_from_update(self):
        defaultColor = Color.objects.create(color="#123ABC", default=True)
        color = Color.objects.create(color="#ABC123")

        color.default = True
        color.save()

        self.assertTrue(Color.objects.get(color="#ABC123").default)
        self.assertFalse(Color.objects.get(color="#123ABC").default)



class RunningTest(TestCase):
    """ Test Running Model """

    def setUp(self):
        self.alarm = Alarm.objects.create(name = 'Test Running', hour = datetime.now().time(), duration = 1, days = '1,2,3', status = True)
        self.running = Running.objects.create(content_object=self.alarm)


    def test_running_color(self):
        color = Color.objects.create(color="#AABBCC")
        running = Running.objects.create(content_object=color)
        self.assertEqual(Running.objects.count(), 1)
        self.assertEqual(str(color), str(running))

    def test_running_alarm(self):
        running = Running.objects.create(content_object=self.alarm)
        self.assertEqual(Running.objects.count(), 1)
        self.assertEqual(str(self.alarm), str(running))