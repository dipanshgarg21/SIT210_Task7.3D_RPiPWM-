#Libraries included
import RPi.GPIO as GPIO
import time

#Raspberry Pi's pins initialised as real numbered pins
GPIO.setmode(GPIO.BOARD)

#Varaibles for the pins numbers of LED and trig, echo pins of the HC SR04
LED = 12
TRIG = 10
ECHO = 8

#Setting distance after which the LED would not give any type of output
MAX_SET_DISTANCE = 20

#Initialised LED and TRIG to output and the ECHO for input as it catches signal outputted from trig
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

#Initialised LED pin to PWM mode so as to control its Duty Cycle
led = GPIO.PWM(LED, 100)
led.start(0)

#calDistance function calculates the overall distance by calcultating the time taken by trig pin's output to be recieved by echo
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
            #Changing the duty cycle as per the percentage calculated
            led.ChangeDutyCycle(100 - (dis/MAX_SET_DISTANCE * 100))
            time.sleep(0.1)
        else:
            led.ChangeDutyCycle(0)
            
except KeyboardInterrupt:
    print("Force Stopped")

#Reset the whole setup once exitted
led.stop()
GPIO.cleanup()
