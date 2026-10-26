#!/usr/bin/env python
"""Control a Raspberry Pi GPIO pin for a specific duration.

This script demonstrates basic GPIO control on a Raspberry Pi by turning
a GPIO pin HIGH for one minute, then turning it back LOW. This can be used
to control an LED, relay, or other electronic component connected to the pin.

Hardware Setup:
    - Connect an LED (with appropriate resistor) or other device to GPIO pin 26
    - Connect the ground wire to a ground pin on the Raspberry Pi

Usage:
    python up_for_a_minute.py

Requirements:
    - RPi.GPIO library
    - Must be run with appropriate permissions (usually requires sudo)

Note:
    The script uses BCM (Broadcom) pin numbering, not physical board numbering.
"""

import time

from RPi import GPIO

# Configuration constants
PIN = 26  # BCM GPIO pin 26 (physical pin 37 on most Pi models)
DELAY = 60  # Duration in seconds (1 minute)

# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

# Configure the pin as an output
GPIO.setup(PIN, GPIO.OUT)

# Turn the pin HIGH (3.3V output)
GPIO.output(PIN, GPIO.HIGH)

# Wait for the specified duration
time.sleep(DELAY)

# Turn the pin LOW (0V output)
GPIO.output(PIN, GPIO.LOW)

# Clean up GPIO resources to reset all pins
GPIO.cleanup()
