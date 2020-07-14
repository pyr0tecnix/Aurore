from django.core.management.base import BaseCommand
from api.models import *


# from gpiozero import LED, Button
from django.core.exceptions import ObjectDoesNotExist


class Command(BaseCommand):
    help = 'Handle I/O'

    def dispatch(self, running):
        if running is None:
            self.stdout.write('none')
        elif(running.content_type == 'alarm'):
            self.stdout.write('alarm')
        elif(running.content_type == 'color'):
            self.stdout.write('color')

    def handle(self, *args, **options):
        self.stdout.write('foo')
        try:
            running = Running.objects.get(id=1)
            self.dispatch(running)
        except ObjectDoesNotExist:
            self.dispatch(None)