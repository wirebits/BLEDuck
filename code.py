# BLEDuck
# Setup for ESP32-S3 boards to make a BLE-enabled USB Rubber Ducky.
# Author - WireBits

import os
import time
import board
import usb_hid
from adafruit_ble import BLERadio
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_ble.services.nordic import UARTService
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement

ble = BLERadio()
uart = UARTService()
advertisement = ProvideServicesAdvertisement(uart)

DEVICE_NAME = "BLEDuck"
advertisement.complete_name = DEVICE_NAME

ble.start_advertising(advertisement)

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

hidKeys = {
    'A': Keycode.A, 'B': Keycode.B, 'C': Keycode.C, 'D': Keycode.D, 'E': Keycode.E,
    'F': Keycode.F, 'G': Keycode.G, 'H': Keycode.H, 'I': Keycode.I, 'J': Keycode.J,
    'K': Keycode.K, 'L': Keycode.L, 'M': Keycode.M, 'N': Keycode.N, 'O': Keycode.O,
    'P': Keycode.P, 'Q': Keycode.Q, 'R': Keycode.R, 'S': Keycode.S, 'T': Keycode.T,
    'U': Keycode.U, 'V': Keycode.V, 'W': Keycode.W, 'X': Keycode.X, 'Y': Keycode.Y,
    'Z': Keycode.Z, 'F1': Keycode.F1, 'F2': Keycode.F2, 'F3': Keycode.F3, 'F4': Keycode.F4,
    'F5': Keycode.F5, 'F6': Keycode.F6, 'F7': Keycode.F7, 'F8': Keycode.F8, 'F9': Keycode.F9,
    'F10': Keycode.F10, 'F11': Keycode.F11, 'F12': Keycode.F12, 'LEFT': Keycode.LEFT_ARROW,
    'UP': Keycode.UP_ARROW, 'RIGHT': Keycode.RIGHT_ARROW, 'DOWN': Keycode.DOWN_ARROW,
    'TAB': Keycode.TAB, 'HOME': Keycode.HOME, 'END': Keycode.END, 'PGUP': Keycode.PAGE_UP,
    'PGDN': Keycode.PAGE_DOWN, 'CAPS': Keycode.CAPS_LOCK, 'NUM': Keycode.KEYPAD_NUMLOCK,
    'SCROLL': Keycode.SCROLL_LOCK, 'CTRL': Keycode.CONTROL, 'SHIFT': Keycode.SHIFT, 'ALT': Keycode.ALT,
    'GUI': Keycode.GUI, 'ESC': Keycode.ESCAPE, 'PRTSCR': Keycode.PRINT_SCREEN, 'PAUSE': Keycode.PAUSE,
    'SPACE': Keycode.SPACE, 'DEL': Keycode.DELETE, 'INSERT': Keycode.INSERT, 'BKSP': Keycode.BACKSPACE,
    'ENTER': Keycode.ENTER, 'APP': Keycode.APPLICATION
}

def convertHID(hidLine):
    newline = []
    for key in filter(None, hidLine.split(" ")):
        key = key.upper()
        command_keycode = hidKeys.get(key, None)
        if command_keycode is not None:
            newline.append(command_keycode)
        elif hasattr(Keycode, key):
            newline.append(getattr(Keycode, key))
        else:
            print("Unknown key! Try another key!")
    return newline

def keyTrigger(hidLine):
    for kd in hidLine:
        kbd.press(kd)
    kbd.release_all()

def typeText(hidLine):
    layout.write(hidLine)

def generateHID(hidScript):
    index = 0
    length = len(hidScript)
    while index < length:
        hidLine = hidScript[index].strip()
        if hidLine.startswith("LOOP"):
            loop_count = int(hidLine.split(" ")[1])
            index += 1
            command_lines = []
            while index < length and hidScript[index].strip() != "EXIT":
                command_lines.append(hidScript[index])
                index += 1
            for _ in range(loop_count):
                for line in command_lines:
                    generateHID([line])
        
        elif hidLine == "INF":
            index += 1
            command_lines = []
            while index < length and hidScript[index].strip() != "EXIT":
                command_lines.append(hidScript[index])
                index += 1
            while True:
                for line in command_lines:
                    generateHID([line])
        elif hidLine == "EXIT":
            break
        else:
            if hidLine.startswith("WAIT"):
                time.sleep(float(hidLine.split(" ")[1]) / 1000)
            elif hidLine.startswith("TYPE"):
                text_to_type = hidLine.split(" ", 1)[1]
                if text_to_type.endswith("-"):
                    typeText(text_to_type[:-1].strip())
                    layout.write("\n")
                else:
                    typeText(text_to_type)
            else:
                newScriptLine = convertHID(hidLine)
                keyTrigger(newScriptLine)
        index += 1

progStatus = False

def hid_execute(hidScript):
    global progStatus
    if not progStatus:
        progStatus = True
        generateHID(hidScript)
        progStatus = False
        print("Done")
    else:
        print("Update your payload and start again!")

def load_hid_script_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return None

while True:
    if ble.connected:
        if uart.in_waiting:
            received = uart.read(1).decode("utf-8").strip()
            if received.isdigit():
                filename = f"payload_{received}.txt"
                hidScript = load_hid_script_from_file(filename)
                if hidScript:
                    hid_execute(hidScript)
        time.sleep(0.1)
    else:
        time.sleep(1)