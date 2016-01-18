#!/usr/bin/python
# -*- coding:utf-8 -*-

import mraa
import time
import math

LED_PIN_NUMBERS = [3, 5, 6, 9]
MIN_VALUE  = 0.0
MAX_VALUE  = 1.0
PWM_INTERVAL = 10000  # 10msec

def map_exp_0_to_255(value):
    v = value * 8.0 / 255.0
    return math.pow(2.0, v) - 1.0

pins = {}

for pin_number in LED_PIN_NUMBERS:
    pin = mraa.Pwm(pin_number)
    pin.period_us(PWM_INTERVAL)
    #pin.enable(True)
    #pin.write(0)
    pins[pin_number] = pin


value = 0
direction = 1

## fade
#while True:
#    #print value
#    for pin in pins:
#        pin.write(value)
#    value = value + 0.01 * direction
#    if value >= MAX_VALUE:
#        value = MAX_VALUE
#        direction = -1
#    elif value <= MIN_VALUE:
#        value = MIN_VALUE
#        direction = 1
#    else:
#        time.sleep(0.05)

## blink
#while True:    
#    for pin in pins:
#        pin.write(1)
#    time.sleep(0.01)
#    for pin in pins:
#        pin.write(0)
#    time.sleep(0.99)

# light on
on_pin_numbers = [3, 5]
for pin_number in LED_PIN_NUMBERS:
    pin = pins[pin_number]
    pin.enable(False)
for pin_number in on_pin_numbers:
    pin = pins[pin_number]
    pin.enable(True)
    pin.write(1)


while True:
    pass
