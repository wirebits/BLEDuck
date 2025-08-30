# BLEDuck boot.py file
# Setup for hide / unhide mass storage device.
# Author - WireBits

import board, storage, digitalio

button=digitalio.DigitalInOut(board.IOX)
button.switch_to_input(pull=digitalio.Pull.UP)

if button.value:
    storage.disable_usb_drive()
