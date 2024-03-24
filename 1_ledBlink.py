
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)   
ledPin = 40   
GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, False)

try:
    while True:
        GPIO.output(ledPin, True)   
        print("LED ON")
        sleep(1)                    
        GPIO.output(ledPin, False)  
        print("LED OFF")
        sleep(1)                    
finally:
   
    GPIO.output(ledPin, False)
    GPIO.cleanup()


