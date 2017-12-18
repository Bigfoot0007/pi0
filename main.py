from sensor import Ultrosensor
import RPi.GPIO as GPIO


U_TRIG1 = 26
U_ECHO1 = 20

U_TRIG2 = 26
U_ECHO2 = 20

U_TRIG3 = 26
U_ECHO3 = 20

MAX_DISTANCE=400

dis1=0
dis2=0
dis3=0



if __name__ == '__main__':
    try:
        Ultrosensor1=Ultrosensor(U_TRIG1,U_ECHO1)
        #Ultrosensor2=Ultrosensor(U_TRIG2,U_ECHO2)
        #Ultrosensor3=Ultrosensor(U_TRIG2,U_ECHO2)
        for i in range(0,101):
            dis1 = Ultrosensor1.distance()
            print(i,dis1)
            #dis2 = Ultrosensor2.distance()
            #dis3 = Ultrosensor3.distance()
            
        GPIO.cleanup()


    except KeyboardInterrupt:
        print("Stopped by User")
        GPIO.cleanup()