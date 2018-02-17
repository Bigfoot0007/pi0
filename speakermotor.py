# -*- coding: utf-8 -*-
'''
  PI Speaker(蜂鸣器) and Motor(震动马达)
'''
import RPi.GPIO as GPIO
import threading
import time
import sys

class SpeakerMotor():
    
    def __init__(self,BEEPPIN,MINIMOTOR,interval=0.1):
        self.beeppin=BEEPPIN  #Motor PIN
        self.minimotor=MINIMOTOR  #Motor PIN
        self.interval=interval   # 设置发声的间隔时间
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.beeppin,GPIO.OUT)
        GPIO.setup(self.minimotor,GPIO.OUT)
        # 初始化两次发音
        GPIO.output(self.beeppin,True)
        GPIO.output(self.minimotor,True)
        time.sleep(1)
        GPIO.output(self.beeppin,False)
        GPIO.output(self.minimotor,False)

          
    def setInterval(self,interval):  # 设置间隔时间
        self.interval=interval
    
    def getInterval(self):  # 设置间隔时间
        return self.interval
    
    def action(self,interval,beeptime,times):
        for a in range(times):
            GPIO.output(self.beeppin,True)
            GPIO.output(self.minimotor,True)
            time.sleep(0.1)
            GPIO.output(self.beeppin,False)
            GPIO.output(self.minimotor,False)
            time.sleep(interval)
            
    def run(self):
        while(1):
            GPIO.output(self.beeppin,False)
            GPIO.output(self.minimotor,False)
            time.sleep(self.interval)
            GPIO.output(self.beeppin,True)
            GPIO.output(self.minimotor,True)
            print(self.beeppin,self.minimotor)
            time.sleep(0.1)
    def stop(self):
        pass
        