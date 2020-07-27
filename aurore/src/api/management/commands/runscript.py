from django.core.management.base import BaseCommand
from api.models import *


# from gpiozero import LED, Button
from django.core.exceptions import ObjectDoesNotExist


class Command(BaseCommand):
    help = 'Handle I/O'

    def dispatch(self, running):
        print(running.content_type)
        if running is None:
            self.stdout.write('none')
        elif(running.content_type == 'api | alarm'):
            self.stdout.write('alarm')
        elif(running.content_type == 'api | color'):
            self.stdout.write('color')

    def handle(self, *args, **options):
        self.stdout.write('foo')
        try:
            running = Running.objects.first()
            self.dispatch(running)
        except ObjectDoesNotExist:
            self.dispatch(None)