#!/usr/bin/env python
"""Blink a Raspberry Pi LED."""

import time

from RPi import GPIO

PIN = 26  # BCM GPIO pin 26
DELAY = 60  # 1 minute

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)
GPIO.output(PIN, GPIO.HIGH)
time.sleep(DELAY)
GPIO.output(PIN, GPIO.LOW)
GPIO.cleanup()
