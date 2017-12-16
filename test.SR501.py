# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

# 测试红外线感应器

# GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.IN)
while 1:
    print("14: "+ str(GPIO.input(14)))
    time.sleep(1)
GPIO.cleanup()