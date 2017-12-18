#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from hcsr04sensor import sensor
import time

trig_pin = 26
echo_pin = 20

beep=16
moder=19

GPIO.setmode(GPIO.BCM)
GPIO.setup(beep, GPIO.OUT)
GPIO.setup(moder, GPIO.OUT)

if __name__ == '__main__':
    try:
        print("==================")
        ti=0;
        while True:
            ti=ti+1
            value = sensor.Measurement(trig_pin, echo_pin)
            raw_measurement = value.raw_distance(sample_size=5, sample_wait=0.03)
            metric_distance = value.distance_metric(raw_measurement)
            print(ti),
            print("The Distance = {} centimeters".format(metric_distance))
            GPIO.output(beep, True)
            GPIO.output(moder, True)
            time.sleep(1)
            GPIO.output(beep, False)
            GPIO.output(moder, False)
            #print("The Distance = {} centimeters".format(raw_measurement))
            #time.sleep(0.1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()