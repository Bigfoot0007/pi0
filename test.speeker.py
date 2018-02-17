#Libraries
import RPi.GPIO as GPIO
import time
from speakermotor import SpeakerMotor

BEEPPIN=16  # Pin8, GPIO14
MINIMOTOR=19  # Õð¶¯Âí´ïPIN

GPIO.setup(BEEPPIN,GPIO.OUT)

if __name__ == '__main__':
    try:
        sm = SpeakerMotor(BEEPPIN,MINIMOTOR)
        sm.start()
        print("==================")

    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()