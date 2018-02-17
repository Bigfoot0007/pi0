# -*- coding: utf-8 -*-
'''
 # 测试峰鸣器
'''
import RPi.GPIO as GPIO
import time

BEEPPIN=16  # Pin8, GPIO14
MINIMOTOR=19  # 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BEEPPIN,GPIO.OUT)
GPIO.setup(MINIMOTOR,GPIO.OUT)
while 1:
    GPIO.output(BEEPPIN,GPIO.LOW)
    GPIO.output(MINIMOTOR,False)
    print("BEEPPIN:LOW")
    time.sleep(2)
    GPIO.output(BEEPPIN,GPIO.HIGH)
    GPIO.output(MINIMOTOR,True)
    print("14:HIGH")
    time.sleep(2)
GPIO.cleanup()