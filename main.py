# -*- coding: utf-8 -*-
from sensor import Ultrosensor
import RPi.GPIO as GPIO
from speakermotor import SpeakerMotor
import time

U_TRIG1 = 26  #超声波发射 PIN
U_ECHO1 = 20  #超声波接受发射波 PIN

BEEPPIN=16  # Pin8, GPIO14
MINIMOTOR=19  # 震动马达PIN

MAX_DISTANCE=400  # 最大测试距离

dis1=0


if __name__ == '__main__':
    try:
        Ultrosensor1=Ultrosensor(U_TRIG1,U_ECHO1)
        sm = SpeakerMotor(BEEPPIN,MINIMOTOR)
        # Ultrosensor2=Ultrosensor(U_TRIG2,U_ECHO2)
        # Ultrosensor3=Ultrosensor(U_TRIG2,U_ECHO2)
        for i in range(0,100000): # 测试1000次
            dis1 = Ultrosensor1.distance1()
            print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),i,dis1)
            if(dis1<60 and dis1 >=50):
                sm.action(0.5,0.1,1)
            elif(dis1<50 and dis1 >=30):
                sm.action(0.25,0.1,2)
            elif(dis1<30):
                sm.action(0.1,0.1,3)
            else:
                pass
            #dis2 = Ultrosensor2.distance()
            #dis3 = Ultrosensor3.distance()
            
        GPIO.cleanup()


    except KeyboardInterrupt:
        print("Stopped by User")
        GPIO.cleanup()
        