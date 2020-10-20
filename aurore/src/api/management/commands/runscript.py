from django.core.management.base import BaseCommand
from api.models import *
from django.core.exceptions import ObjectDoesNotExist
from api.scripts import drive_white_led

#Only for testing purpose
from gpiozero.pins.mock import MockFactory

from gpiozero import Device, LED, Button


class Command(BaseCommand):
    help = 'Handle I/O'
    # Set the default pin factory to a mock factory
    Device.pin_factory = MockFactory()

    led = LED(17)

    drive_white_led(17)
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