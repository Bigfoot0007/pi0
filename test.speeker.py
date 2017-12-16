#Libraries
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
BEEPPIN=14  # Pin8, GPIO14

GPIO.setup(BEEPPIN,GPIO.OUT)

if __name__ == '__main__':
    try:
        print("==================")
        while True:
            GPIO.output(BEEPPIN, False)
            time.sleep(0.00001)
            GPIO.output(BEEPPIN, True)
            time.sleep(0.0001)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()