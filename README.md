<img width="2048" height="2048" alt="BLEDuck" src="https://github.com/user-attachments/assets/9a27426b-f0c5-435c-aeed-39dadd84e207" />

# 🦆BLEDuck
A BLE-controlled USB Rubber Ducky clone built with ESP32-S3 boards.

# ✨Features
- Minimal Setup.
- Simply controlled by Serial Bluetooth Terminal App.
- Execute payloads by just sending numbers.
- Store payloads in folder for better management.
- Hide / Unhide mass storage device for stealth.

# 👍Recommended
- Use those ESP32-S3 boards which has at least `8MB` flash memory.

# ⚙️Setup ESP32-S3 boards for CircuitPython
1. Open Official CircuitPython download link from [here](https://circuitpython.org/downloads).
2. Search `ESP32-S3` according to the board you have.
3. Select your board and click on it.
4. At the end of the page, there is button named `DOWNLOAD BOOTLOADER combined.bin`.
5. Click on it to download.
   - There is a file named `tinyuf2-<NAME-OF-BOARD>-0.35.0-combined.bin`.
6. Open Adafruit ESP Web Flasher from [here](https://adafruit.github.io/Adafruit_WebSerial_ESPTool/).
7. Connect `ESP32-S3` with a USB cable and then to the PC/Laptop.
8. Press and hold the `BOOT` button.
9. Press and release the `RST` button.
10. Release the `BOOT` button.
11. Set the Baud Rate to `460800 Baud`.
12. Click on `Connect` button.
13. Select your Device COM Port in the Pop-Up Window.
14. Click on `Connect` button in the Pop-Up Window.
   - When connected successfully, then it show this ![image](https://github.com/user-attachments/assets/3dd86d85-df80-4d58-aba5-e078dc30212c)
15. Click on `Erase` button.
16. Wait for sometimes to successfully erased.
17. Click on first one `Choose a file...`.
18. Select the `tinyuf2-<NAME-OF-BOARD>-0.35.0-combined.bin` file.
19. Click on `Program` button.
20. Wait for sometimes and after successfully flashed, press and release the `RST` or `RESET` button.
21. Plug-out and then plug-in the USB cable in PC/Laptop.
   - When it connects, then `ESP32-S3` board as a removable storage device `S3DKC1BOOT`.
22. Done! Now, `ESP32-S3` Board is ready to flash CircuitPython `.uf2` file.

# ⚙️Setup CircuitPython
1. Open Official CircuitPython download link from [here](https://circuitpython.org/downloads).
2. Search `ESP32-S3` according to the board you have.
3. Select your board and click on it.
4. Download latest stable release CircuitPython `.uf2` file and noted its version.
   - It is like `X.Y.Z`.
   - Latest stable release is `9.2.8` but it can be changed in future so keep eye on it.
5. Copy the `.uf2` file into the `S3DKC1BOOT`.
   - When it is copied, then it disconnects automatically and reconnect as `CIRCUITPY`.
   - Means CircuitPython is successfully flashed in the `ESP32-S3` board.
6. Done! Now, `ESP32-S3` Board is flashed with CircuitPython `.uf2` file.

# ⚙️Setup Essential Files for BLEDuck
1. Download or Clone the Repository.
2. Open the folder.
   - Make sure that your `ESP32-S3` board is connected to your PC/Laptop.
3. Copy `code.py` in the `CIRCUITPY`.
   - It ask for replacement of `code.py` file, then replace it.
   - It will overwrite in the `code.py` file.
4. Copy `boot.py` in the `CIRCUITPY`.
5. Download latest Adafruit CircuitPython Bundle from [here](https://circuitpython.org/libraries).
   - There are 2 variants of libraries : `Bundles` and `The Community Bundle`.
   - In `Bundles` variant, download latest stable Adafruit CircuitPython Bundle as noted version of `.uf2` file.
   - Latest stable release is `adafruit-circuitpython-bundle-9.x-mpy-20250829.zip` but it can be changed in future so keep eye on it.
6. Extarct the ZIP file.
7. Go to the `lib` folder in the extracted ZIP file.
8. Copy `adafruit_ble` and `adafruit_hid` folders in the `lib` folder of `CIRCUITPY`.
    - After 2-3 minutes, an BLE device named `BLEDuck` is discovered.
9. Create a folder named `payloads` in `CIRCUITPY`.
10. Done! Now, `ESP32-S3` board is ready to use as a BLEDuck.

# 📄Payload Files
1. Open Notepad or any other text editor.
2. Write your payload in it.
3. When saving the file, select `CIRCUITPY`.
4. Then go to the `payloads` folder.
5. Name the payload as `payload-1`, `payload-2` etc.
   - It is saved by default as `.txt` files.

# 🧩CIRCUITPY Directory Structure
- **CIRCUITPY/**
  - **lib/**
      - `adafruit_ble`
      - `adafruit_hid`
  - `code.py`
  - `boot.py`
  - **payloads/**
    - `payload-X.txt`
  - where `X` is a number like `1`,`2`,`3`,`4` etc.

# 🏃🏻‍♂Run BLEDuck
1. Turn on your mobile bluetooth.
2. Scan the bluetooth and it show `BLEDuck`.
3. Connect and pair with it.
4. Download `Serial Bluetooth Terminal` app from [here](https://play.google.com/store/apps/details?id=de.kai_morich.serial_bluetooth_terminal).
5. Open `Serial Bluetooth Terminal` app.
8. Click on `☰`.
9. Click on `Devices`.
10. Click on `Bluetooth LE`.
11. Click on `Scan`.
    - It ask for permission, then click on `Allow`.
    - There is a device named `BLEDuck` show in it.
12. Click on it.
13. After that, when it show `Connected` it means ready to execute payloads using BLE.
14. Just type the number and click on Send button.
    - The payload of that number executes immediately.

# 💡Mnemonic Table
| Mnemonics | Description | Example  |
|-----------|-------------|----------|
| WAIT      | It add time in the code.<br>Time is in milliseconds.<br>1000 ms = 1 second. | WAIT 1000 |
| TYPE      | It add text want to type in the code. | TYPE Hello World! |
| LOOP      | It runs commands for a certain number of times.<br> Synatx is `LOOP number-of-times commands` | LOOP 3<br>TYPE Hello World!<br>EXIT<br><br>LOOP 4<br>TAB<br>EXIT<br><br>LOOP 1<br>CTRL S<br>EXIT<br><br>LOOP 1<br>CTRL SHIFT N<br>EXIT<br> |
| INF       | It run commans infinitely.<br>Syntax is `INF commands` | INF<br>TYPE Hello World!<br>EXIT<br><br>INF<br>TAB<br>EXIT<br> |

# 🔡Special Symbols
1. `-`
- It is used to put the cursor in the next line.
- It is only used with TYPE.
- Example : `TYPE Hello World!-`
- If TYPE contain any command and then `-` then it run automatically without `ENTER` key.

# 📝Supported Mnemonics
## Alphabet Keys
`A` `B` `C` `D` `E` `F` `G` `H` `I` `J` `K` `L` `M` `N` `O`
`P` `Q` `R` `S` `T` `U` `V` `W` `X` `Y` `Z`
## Function Keys
`F1` `F2` `F3` `F4` `F5` `F6` `F7` `F8` `F9` `F10` `F11` `F12`
## Navigation Keys
`LEFT` `UP` `RIGHT` `DOWN` `TAB` `HOME` `END` `PGUP` `PGDN`
## Lock Keys
`CAPS` `NUM` `SCROLL`
## System and GUI Keys
`GUI` `ESC` `PRTSCR` `PAUSE`
## Editing Keys
`INSERT` `DEL` `BKSP` `ENTER`
## Modifier Keys
`CTRL` `SHIFT` `ALT`
## ASCII Characters
`` ` `` `!` `@` `#` `$` `%` `^` `&` `*` `(` `)` `-` `=` `[` `]` `\` `;` 
`'` `,` `.` `/` `SPACE` `~` `_` `+` `{` `}` `|` `:` `"` `<` `>` `?` `0`
`1` `2` `3` `4` `5` `6` `7` `8` `9`

# 📖Examples
## Open notepad and type Hello World!

```
WAIT 1000
GUI R
WAIT 1000
TYPE notepad
WAIT 1000
ENTER
WAIT 1000
TYPE Hello World!
```
## Open CMD as Administrator Mode

```
WAIT 1000
GUI R
WAIT 1000
TYPE cmd
WAIT 1000
CTRL SHIFT ENTER
WAIT 1300
ALT Y
```
## Create A New Folder
```
WAIT 1000
CTRL SHIFT N
WAIT 1200
TYPE hello
WAIT 1100
ENTER
```
## Open notepad and type Hello World! 6 times in different lines
```
WAIT 1000
GUI R
WAIT 1000
TYPE notepad
WAIT 1000
ENTER
WAIT 1000
LOOP 6
TYPE Hello World!-
EXIT
```
