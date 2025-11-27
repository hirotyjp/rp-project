# Remote BitLocker PIN Unlocker

This project provides a way to unlock a BitLocker-protected PC remotely using a Raspberry Pi 2 and an RP2040.
The Raspberry Pi 2 sends the PIN to the RP2040 over UART, and the RP2040—connected to the target PC—acts as a USB keyboard to input the PIN automatically.

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

  - Raspberry PI (I use RP2 model B)
    - Raspbian (Bullseye)
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

   - RP2B and RP2040 cannot detect when to start sending the PIN.
     This means the PIN must be sent immediately after the PC powers on. In some cases, BitLocker may time out and force the PC to power off before the PIN is entered.
   - Software UART is unstable.
     It sometimes receives noise from nearby systems, causing incorrect keycodes to be sent. If needed, you can disable the software UART and use only the hardware UART. I have not tested it, but the Raspberry Pi 4 has multiple hardware UART interfaces (including several Mini UARTs), so replacing the current software UART with a hardware UART should be possible on other Pi models.
   - Entering a wrong PIN cannot be corrected.
     If an incorrect PIN is sent and BitLocker rejects it, you cannot delete the input because this program currently does not support DEL or Backspace keys. As a result, you may need to wait until the PC powers off due to timeout.

## Issues

   - After a few weeks since I setup the system, I have found that RP2040 was stuck with something and keeping a red LED blinking. It became no longer receive any command and didn't send any PIN as well. The root cause is still unknown, but I suspect that an unexpected shutdown for PC causes the issue. I tried to disable the USB mass-storage by `boot.by` just in case, and still investigating.
   - If disabling USB mass-storage cannot solve the issue, sending force Reset command to RP2040 would be one of the solutions. But RP2040 Pico Zero I bought doesn't have GPIO30, RUN PIN. So I will need to connect the wire to the physical Reset Button with soldering. It might be a bit challenging as that button is very small.  
