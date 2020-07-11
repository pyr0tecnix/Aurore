from django.test import TestCase
from django.core.exceptions import ObjectDoesNotExist
from api.models import Alarm, Color

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

