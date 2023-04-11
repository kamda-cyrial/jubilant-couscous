import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 50)  # Use 50 Hz frequency for the PWM signal
p.start(0)

def clockwise():
    p.ChangeDutyCycle(2.5)  # Rotate the servo clockwise to pull down the syringe
    time.sleep(2.5)
    p.ChangeDutyCycle(0)  # Stop the servo for 3 seconds
    time.sleep(3)

def counterclockwise():
    p.ChangeDutyCycle(11.5)  # Rotate the servo counterclockwise to pull up the syringe
    time.sleep(2.5)
    p.ChangeDutyCycle(0)  # Stop the servo

try:
    while True:
        clockwise()
        counterclockwise()

except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()