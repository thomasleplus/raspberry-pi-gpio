# Raspberry Pi GPIO

A simple example of how to control a Raspberry Pi's GPIO pin using Python. This project demonstrates basic GPIO control by turning a pin HIGH for one minute, then LOW, making it perfect for controlling LEDs, relays, or other electronic components.

## Overview

The `up_for_a_minute.py` script provides a straightforward example of GPIO control on the Raspberry Pi. It uses the RPi.GPIO library to control GPIO pin 26 (BCM numbering), turning it on for 60 seconds before turning it off and cleaning up resources.

## Hardware Requirements

- Raspberry Pi (any model with GPIO pins)
- LED (optional) with appropriate current-limiting resistor (typically 220Ω-330Ω)
- Jumper wires
- Breadboard (optional, for prototyping)

## Software Requirements

- Python 3.x
- RPi.GPIO library

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/raspberry-pi-gpio.git
   cd raspberry-pi-gpio
   ```

2. Install the RPi.GPIO library (if not already installed):

   ```bash
   pip install RPi.GPIO
   ```

   Or on most Raspberry Pi systems:

   ```bash
   sudo apt-get update
   sudo apt-get install python3-rpi.gpio
   ```

## Hardware Setup

### Basic LED Connection

1. Connect the **anode** (longer leg) of the LED to **GPIO pin 26** (physical pin 37)
2. Connect a **220Ω-330Ω resistor** in series with the LED
3. Connect the **cathode** (shorter leg) of the LED to any **GND** pin

```text
Raspberry Pi          LED
GPIO 26 (Pin 37) -->  Anode (+) --|>|-- Resistor -- GND
```

**Note:** The script uses BCM (Broadcom) pin numbering. GPIO 26 in BCM mode corresponds to physical pin 37 on the 40-pin header.

## Usage

Run the script with Python 3:

```bash
python up_for_a_minute.py
```

Or with sudo if you encounter permission issues:

```bash
sudo python up_for_a_minute.py
```

The script will:

1. Turn GPIO pin 26 HIGH (3.3V)
2. Wait for 60 seconds
3. Turn GPIO pin 26 LOW (0V)
4. Clean up GPIO resources

## Configuration

You can modify the constants at the top of `up_for_a_minute.py` to customize the behavior:

- `PIN`: Change the GPIO pin number (BCM numbering)
- `DELAY`: Change the duration in seconds

Example:

```python
PIN = 17  # Use GPIO 17 instead
DELAY = 30  # Run for 30 seconds instead of 60
```

## Pin Numbering

This script uses **BCM (Broadcom)** pin numbering, which refers to the GPIO numbers on the Broadcom chip. This is different from the physical pin numbers on the board.

Common BCM GPIO pins:

- GPIO 26 = Physical Pin 37
- GPIO 17 = Physical Pin 11
- GPIO 27 = Physical Pin 13

For a complete pinout diagram, visit [pinout.xyz](https://pinout.xyz/)

## Troubleshooting

### Permission Denied

If you get a permission error, run the script with sudo:

```bash
sudo python up_for_a_minute.py
```

### GPIO Already in Use

If you see warnings about GPIO channels already in use, the cleanup wasn't properly executed. You can force cleanup by running:

```python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
```

### LED Not Lighting

- Check the LED polarity (longer leg is positive/anode)
- Verify the resistor is connected
- Ensure you're using the correct pin number
- Test the LED with a multimeter or battery

## Safety Notes

- Always use current-limiting resistors with LEDs
- Raspberry Pi GPIO pins output 3.3V (not 5V)
- Maximum current per GPIO pin: ~16mA
- Never connect GPIO pins directly to 5V or ground without appropriate circuitry

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## Security

Please read [SECURITY.md](SECURITY.md) for details on our security policy and how to report security vulnerabilities.

## Code of Conduct

Please read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for details on our code of conduct.
