import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

LED = 12
TRIG = 10
ECHO = 8

MAX_SET_DISTANCE = 20

GPIO.setup(LED, GPIO.OUT)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

led = GPIO.PWM(LED, 100)
led.start(0)

def calDistance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == False:
        start = time.time()

    while GPIO.input(ECHO) == True:
        end = time.time()

    sig_time = end-start
    
    distance = sig_time / 0.000058
    return distance

try:
    while 1:
        dis = calDistance()
        print(dis)
        if dis <= MAX_SET_DISTANCE:
            led.ChangeDutyCycle(100 - (dis/MAX_SET_DISTANCE * 100))
            time.sleep(0.1)
        else:
            led.ChangeDutyCycle(0)
            
except KeyboardInterrupt:
    print("Force Stopped")

led.stop()
GPIO.cleanup()
