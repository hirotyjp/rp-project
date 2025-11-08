# Remote Bitlocker PIN unlocker

This project is to unlock Bitlcoker PIN remotely, using RP2 and RP2040.
You can send the PIN via UART from RP2, and it will be sent to RP2040. RP2040 have to be connected to PC, and it inputs the PIN as USB Keyboard.

## Connections

    Physical Connections
    --------------------
    
            RP2B ----- H/W UART --- RP2040 #1 --- PC1
               |
               +------ S/W UART --- RP2040 #2 --- PC2
        
            H/W UART TX (GPIO 14)  ---- RP2040 #1 RX (GPIO 1)
                     GND (Pin 6)   ---- RP2040 #1 GND

            S/W UART TX (GPIO 26)  ---- RP2040 #2 RX (GPIO 1)
                     GND (Pin 39)  ---- RP2040 #1 GND

    PIN Layout for RP2B
    -------------------
                                    J8:
                                   3V3  (1) (2)  5V
                                 GPIO2  (3) (4)  5V
                                 GPIO3  (5) (6)  GND     --------- RP2040 #1 GND
                                 GPIO4  (7) (8)  GPIO14  --------- RP2040 #1 RX
                                   GND  (9) (10) GPIO15
                                GPIO17 (11) (12) GPIO18
                                GPIO27 (13) (14) GND
                                GPIO22 (15) (16) GPIO23
                                   3V3 (17) (18) GPIO24
                                GPIO10 (19) (20) GND
                                 GPIO9 (21) (22) GPIO25
                                GPIO11 (23) (24) GPIO8
                                   GND (25) (26) GPIO7
                                 GPIO0 (27) (28) GPIO1
                                 GPIO5 (29) (30) GND
                                 GPIO6 (31) (32) GPIO12
                                GPIO13 (33) (34) GND
                                GPIO19 (35) (36) GPIO16
      RP2040 #2 RX   ---------  GPIO26 (37) (38) GPIO20
      RP2040 #2 GND  ---------     GND (39) (40) GPIO21


## Requirements

  - Rapsberry PI (I use RP2 model B)
    - Raspbian (Bulluseye)
    - pigpiod (for S/W UART)
  
  - RP2040
    - CircuitPython
    - HID Library
    - Neopixel Library

## Usage

   - Connect RP2040 to PC and write CicruitPython.
   - Put `code.py` into RP2040
   - Connect all above physical lines
   - Connect RP2 via ssh
   - Turn on PC via Wake on LAN
   - Run shell script, and input the PIN
   - PIN will be sent to PC !!

## Limitations

   - RP2B and RP2040 cannot know when they can start sending the PIN, it means you need to input the PIN as soon as PC is up. Sometimes BitLocker is timed out and PC is turned power off.
   - Software UART is quite unstable, it receives some noises sometimes from surrunded systems, and it inputs strange Keycode oftenly. If necessary you can disable it and use only Hardware UART. I have never tested but RP4 has many Hardware UART (several Mini UART), it would be possible to replace the current Software UART with Hardware UART in case other RPs.
