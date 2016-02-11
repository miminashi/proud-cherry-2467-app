#!/usr/bin/python
# -*- coding:utf-8 -*-

import mraa
import time
import math
import signal

LED_PIN_NUMBERS = [3, 5, 6, 9]
MIN_VALUE  = 0.0
MAX_VALUE  = 1.0
PWM_INTERVAL = 10000  # 10msec

# value is 0 ~ 255
def map_exp_0_to_255(value):
    v = value * 8.0 / 255.0
    return math.pow(2.0, v) - 1.0

# maps 0 ~ 255 -> 0 ~ 1.0
def map_255_to_1(value):
    return value / 255.0

def get_pins():
    pins = {}
    for pin_number in LED_PIN_NUMBERS:
        pin = mraa.Pwm(pin_number)
        pin.period_us(PWM_INTERVAL)
        pin.enable(True)
        pin.write(0.0)
        pins[pin_number] = pin
    return pins

def write_pins(pins, value):
    for pin_number, pin in pins.iteritems():
        pin.write(map_255_to_1(map_exp_0_to_255(value)))

def write_pins_and_wait(pins, value):
    write_pins(pins, value)
    time.sleep(0.01)

def disable_pins(pins):
    for pin_number, pin in pins.iteritems():
        pin.enable(False)

def exit_signal_handler(signo, frame):
    pins = get_pins()
    disable_pins(pins)
    time.sleep(0.5)
    print("exitting...")
    exit()

# register signal handlers
signal.signal(signal.SIGHUP, exit_signal_handler)
signal.signal(signal.SIGINT, exit_signal_handler)
signal.signal(signal.SIGTERM, exit_signal_handler)

# get pins
pins = get_pins()

# fade
while True:
    for x in xrange(255):
        write_pins_and_wait(pins, x)
    for x in xrange(255, 0, -1):
        write_pins_and_wait(pins, x)

## blink
#while True:    
#    for pin in pins:
#        pin.write(1)
#    time.sleep(0.01)
#    for pin in pins:
#        pin.write(0)
#    time.sleep(0.99)

## light on
#write_pins(pins, 255)
#while True:
#    continue

