# BLEDuck boot.py file
# Setup for hide / unhide mass storage device and disable serial console.
# Author - WireBits

import board, storage, digitalio, usb_cdc

button=digitalio.DigitalInOut(board.IOX)
button.switch_to_input(pull=digitalio.Pull.UP)

if button.value:
    usb_cdc.disable()
    storage.disable_usb_drive()
