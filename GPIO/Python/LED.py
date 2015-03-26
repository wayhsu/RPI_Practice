#!/usr/bin/python
import RPi.GPIO as GPIO
import time

# Use physical pin numbers
GPIO.setmode(GPIO.BOARD)
# Set up header pin 12 (GPIO18) as an input
ledPin = 7
print "Setup Pin 12 is OutPut..."
GPIO.setup(ledPin, GPIO.OUT)

print "Starting... "
while True:
  print "Set Output False"
  GPIO.output(ledPin, False)
  time.sleep(1)
  print "Set Output True"
  GPIO.output(ledPin, True)
  time.sleep(1)