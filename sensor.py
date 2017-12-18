# -*- coding: utf-8 -*-
'''
  PI Sensor Speeker, Rumble Motor
'''
import RPi.GPIO as GPIO
import time

class Ultrosensor(object):
    
    def __init__(self, U_TRIG1, U_ECHO1, MixDistance=4, MaxDistance = 500.0):
        self.trig=U_TRIG1
        self.echo=U_ECHO1
        self.timeout=(MaxDistance/34300)*5  # timeout 
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trig, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)
    
    def distance(self):
        # set Trigger to HIGH, and set Trigger after 0.01ms to LOW
        # GPIO.output(self.trig, False)
        GPIO.output(self.trig, True)
        time.sleep(0.00001)
        GPIO.output(self.trig, False)
     
        StartTime = time.time()
        StopTime = time.time()
        # save StartTime
        while GPIO.input(self.echo) == 0:
            now1=time.time()
            #print(GPIO.input(self.echo)),
            #print(time.time(),StartTime,(time.time() - StartTime),self.timeout)
            if((time.time() - StartTime) >= self.timeout):
                StartTime = time.time()
            else:
                break
        
        # save time of arrival
        while GPIO.input(self.echo) == 1:
            #print(GPIO.input(self.echo)),
            StopTime = time.time()
            
        TimeElapsed = StopTime - StartTime
        # print("StartTime: %f - %f = %f" % (StartTime,StopTime,TimeElapsed))
        # time difference between start and arrival
        
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = round((TimeElapsed * 34300) / 2)
     
        return distance

    
    
