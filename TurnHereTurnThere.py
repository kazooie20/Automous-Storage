import l293d
from time import sleep
from gpiozero import Motor
import RPi.GPIO as GPIO
import sys

#Flask
from flask import Flask, request, abort
import json

def runMotor():
    # Motor 1 uses Pin 22, Pin 18, Pin 16
    motor1 = l293d.DC(22,18,16)
    # Run the motors so visible
    for i in range(0,300):
      motor1.anticlockwise()

    l293d.cleanup()


def slowMotor():
    motorA = Motor(22,18,16)
    motorA.forward(0.5)
    sleep(2)
    motorA.stop()
    print "Motor running...."

def SlowDown():
    GPIO.setmode(GPIO.BOARD)
    Motor1A = 22
    Motor1B = 18
    Motor1E = 16

    GPIO.setup(Motor1A,GPIO.OUT)
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor1E,GPIO.OUT)

    pwm = GPIO.PWM(Motor1E,100)
    pwm.start(0)
    

    print "Forwards"
    GPIO.output(Motor1A,True)
    GPIO.output(Motor1B,False)

    pwm.ChangeDutyCycle(70)
    
    GPIO.output(Motor1E,True)

    sleep(1)

    GPIO.output(Motor1E,False)



    pwm.ChangeDutyCycle(50)
    
    GPIO.output(Motor1E,True)

    sleep(5)

    GPIO.output(Motor1E,False)
    pwm.stop()

    
    
    GPIO.cleanup()
    sys.exit()

def Move_One_Compt():
    
    GPIO.setmode(GPIO.BOARD)
    Motor1A = 22
    Motor1B = 18
    Motor1E = 16

    GPIO.setup(Motor1A,GPIO.OUT)
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor1E,GPIO.OUT)

    pwm = GPIO.PWM(Motor1E,100)
    pwm.start(0)
    

    
    GPIO.output(Motor1A,True)
    GPIO.output(Motor1B,False)

    pwm.ChangeDutyCycle(70)
    
    GPIO.output(Motor1E,True)

    sleep(0.8)

    GPIO.output(Motor1E,False)
    pwm.stop()

    
    
    GPIO.cleanup()
    sys.exit()

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    Move_One_Compt()
    return 'going!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')




