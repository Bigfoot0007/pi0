# -*- coding: utf-8 -*-
'''
 # 测试峰鸣器
'''
import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.OUT)
while 1:
    GPIO.output(14,GPIO.LOW)
    print("14:LOW")
    time.sleep(2)
    GPIO.output(14,GPIO.HIGH)
    print("14:HIGH")
    time.sleep(2)
GPIO.cleanup()