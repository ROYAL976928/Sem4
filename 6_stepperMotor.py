import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

stepPin1 = 31
stepPin2 = 33
stepPin3 = 35
stepPin4 = 37

GPIO.setup(stepPin1, GPIO.OUT)
GPIO.setup(stepPin2, GPIO.OUT)
GPIO.setup(stepPin3, GPIO.OUT)
GPIO.setup(stepPin4, GPIO.OUT)

GPIO.output(stepPin1, False)
GPIO.output(stepPin2, False)
GPIO.output(stepPin3, False)
GPIO.output(stepPin4, False)

def singleStep(stepVal1, stepVal2, stepVal3, stepVal4):
    GPIO.output(stepPin1, stepVal1)
    GPIO.output(stepPin2, stepVal2)
    GPIO.output(stepPin3, stepVal3)
    GPIO.output(stepPin4, stepVal4)
    
def clockWiseRotate(delay, steps1):
    for i in range (0, steps1):
        singleStep(1, 0, 0, 0)
        time.sleep(delay)
        singleStep(1, 1, 0, 0)
        time.sleep(delay)
        singleStep(0, 1, 0, 0)
        time.sleep(delay)
        singleStep(0, 1, 1, 0)
        time.sleep(delay)
        singleStep(0, 0, 1, 0)
        time.sleep(delay)
        singleStep(0, 0, 1, 1)
        time.sleep(delay)
        singleStep(0, 0, 0, 1)
        time.sleep(delay)
        singleStep(1, 0, 0, 1)
        time.sleep(delay)

def anticlockWiseRotate(delay, steps2):
    for i in range (0, steps2):
        singleStep(1, 0, 0, 1)
        time.sleep(delay)
        singleStep(0, 0, 0, 1)
        time.sleep(delay)
        singleStep(0, 0, 1, 1)
        time.sleep(delay)
        singleStep(0, 0, 1, 0)
        time.sleep(delay)
        singleStep(0, 1, 1, 0)
        time.sleep(delay)
        singleStep(0, 1, 0, 0)
        time.sleep(delay)
        singleStep(1, 1, 0, 0)
        time.sleep(delay)
        singleStep(1, 0, 0, 0)
        time.sleep(delay)
        
try:
    while 1:
        delay = input("Enter delay betwwen steps (in miliseconds): ")
        steps1 = input("How many steps clockwise?: ")
        steps2 = input("How many steps Anticlcokwise?: ")
        clockWiseRotate(int(delay)/1000.0, int(steps2))
        anticlockWiseRotate(int(delay)/1000.0, int(steps2))
        
        
finally:
    GPIO.cleanup()

        
