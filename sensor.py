# -*- coding: utf-8 -*-
'''
  PI Sensor Ultrosensor 采用 HC-SR04，该模块，需要执行好提供10us的高电平。
   发出8个40kHz的超声波，然后等待返回。
'''
import RPi.GPIO as GPIO
import time
import sys

class Ultrosensor(object):
    
    def __init__(self, U_TRIG1, U_ECHO1, MixDistance=4, MaxDistance = 500.0):
        self.trig=U_TRIG1
        self.echo=U_ECHO1
        self.timeout=(MaxDistance/34300)*5  # timeout，MaxDistance unit is CM
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trig, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)
    
    def distance(self):
        # set Trigger to HIGH, and set Trigger after 0.01ms to LOW
        # GPIO.output(self.trig, False)
        time.sleep(0.02)  # 默认暂停0.02后开始测试，这样1秒可以测试近50次。
        GPIO.output(self.trig, False)
        GPIO.output(self.trig, True)
        time.sleep(0.00001)
        GPIO.output(self.trig, False)
        sys.stdout.write(str("S"))
        StartTime = time.time()
        StopTime = StartTime
        # save StartTime
        while GPIO.input(self.echo) == 0:
            sys.stdout.write(str("_"))
            now1=time.time()
            #print(GPIO.input(self.echo)),
            # print(time.time(),StartTime,(time.time() - StartTime),self.timeout)
            if((now1 - StartTime) >= self.timeout):
                StartTime = now1
            else:
                break
        
        # save time of arrival
        while GPIO.input(self.echo) == 1:
            StopTime = time.time()
            sys.stdout.write(str("-"))
            
        TimeElapsed = StopTime - StartTime
        # print("StartTime: %f - %f = %f" % (StartTime,StopTime,TimeElapsed))
        
        # time difference between start and arrival
        # multiply with the sonic speed (34300 cm/s) and divide by 2, because there and back
        distance = round((TimeElapsed * 34300) / 2)
     
        return distance
    
    def distance1(self):
        # set Trigger to HIGH, and set Trigger after 0.01ms to LOW GPIO.output(self.trig, False)
        time.sleep(0.02)  # 默认暂停0.02后开始测试，这样1秒可以测试近50次。
        GPIO.output(self.trig, False) # 先设置低电平，相当于初始化操作
        GPIO.output(self.trig, True) # 设置高电平
        time.sleep(0.000015)  # 持续10us， HC-SR04基本原理，至少需要10us，为了准确，这里给15us
        GPIO.output(self.trig, False) # 关闭发送
        sys.stdout.write(str("S"))
        StartTime=StopTime = time.time()  # 记录时间，这个时候开始时间和结束时间一致。
        uptime=downtime=0;  #记录有无信号变化。uptime表示变为高电平，downtime表示变为低电平
        while(StopTime-StartTime<self.timeout): # 如果为超时，则继续探测时间。
            # sys.stdout.write(str(GPIO.input(self.echo)))
            StopTime=time.time() # 记录一次时间，作为Stoptime
            if(GPIO.input(self.echo) == 0 and uptime >1 and downtime ==0):
                downtime=StopTime
                sys.stdout.write(str("D"))
                break;
            if(GPIO.input(self.echo) == 1 and downtime ==0 and uptime==0):
                uptime=StopTime
                sys.stdout.write(str("U"))
                
        if(StopTime-StartTime>=self.timeout): # 如果超时，不做计算机，直接返回 T
            sys.stdout.write(str("T"))
            downtime=StopTime
            return "T"
        if(downtime>uptime):
            TimeElapsed = downtime - uptime
            distance = round((TimeElapsed * 34300) / 2)
            return distance
        

    def status(self):
        StartTime = time.time()
        StopTime = StartTime
        while(1):
            StopTime = time.time()
            if(StopTime-StartTime>=1):
                StartTime = StopTime
                print("\n\n")
            if(GPIO.input(self.echo)==0):
                sys.stdout.write(str("_"))
            else:
                sys.stdout.write(str("-"))
                
    # 测试函数，发送后，进行1000次探测，并打印返回。
    def test(self):
        GPIO.output(self.trig, True)
        time.sleep(0.00001)
        GPIO.output(self.trig, False)
        sys.stdout.write(str("S"))
        StartTime = time.time()
        StopTime = StartTime
        for i in range(1000):
            if(GPIO.input(self.echo)==0):
                sys.stdout.write(str(" "))
            else:
                sys.stdout.write(str("-"))
        print("\n")