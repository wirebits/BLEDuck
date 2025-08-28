# BLEDuck boot.py file
# Setup for ESP32-S3 boards to make a BLE-enabled USB Rubber Ducky.
# Author - WireBits

import board, storage, digitalio

button=digitalio.DigitalInOut(board.IOX)
button.switch_to_input(pull=digitalio.Pull.UP)

if button.value:
    storage.disable_usb_drive()