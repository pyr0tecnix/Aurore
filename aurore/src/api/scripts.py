from gpiozero import Device, LED, Button
from gpiozero.pins.mock import MockPin

def drive_white_led(pin):
    led = Device.pin_factory.pin(pin)
    current_value = led._get_state()

    print(current_value)
    value = (current_value + 0.25)%1
    print('Value : {}'.format(value))
    led._set_state((current_value + 0.25)%1)

def drive_rgb_led(red_pin, green_pin, blue_pin):