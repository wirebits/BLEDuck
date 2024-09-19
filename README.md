# BLEDuck
Setup for ESP32-S3 boards to make a BLE-enabled USB Rubber Ducky.

# Key Features
- Minimal Setup.
- Simply controlled by Serial Bluetooth Terminal App.
- Execute payloads by just sending numbers.

# OS Support
- Windows 10
- Android

# Setup of ESP32-S3
1. Open Official CircuitPython download link from [here](https://circuitpython.org/downloads).
2. Search `ESP32-S3`.
3. Select your board and click on it.
4. At the end of the page, there is button named `DOWNLOAD BOOTLOADER ZIP`.
5. Click on it to download.
6. Open that ZIP file.
7. There is a file named `combined.bin`.
8. Open Adafruit ESP Web Flasher from [here](https://adafruit.github.io/Adafruit_WebSerial_ESPTool/).
9. Connect ESP32-S3 with a USB cable.
10. Connect to the PC/Laptop.
11. Press and hold the `BOOT` button.
12. Press and release the `RST` button.
13. Release the `BOOT` button.
14. Set the Baud Rate to `460800 Baud`.
15. Click on `Connect` button.
16. Select your Device COM Port in the Pop-Up Window.
17. Click on `Connect` button in the Pop-Up Window.
   - When connected successfully, then it show this ![image](https://github.com/user-attachments/assets/3dd86d85-df80-4d58-aba5-e078dc30212c)
18. Click on `Erase` button.
19. Wait for sometimes to successfully erased.
20. Click on first one `Choose a file...`.
21. Select the `combined.bin` file.
22. Click on `Program` button.
23. Wait for sometimes and after successfully flashed, press and release the `RST` button.
24. Done! Now, ESP32-S3 Board is ready to flash CircuitPython `.uf2` file.
