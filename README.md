# Remote Bitlocker PIN unlocker

This project is to unlock Bitlcoker PIN remotely, using RP2 and RP2040.
You can send the PIN via UART from RP2, and it will be sent to RP2040. RP2040 have to be connected to PC, and it inputs the PIN as USB Keyboard.

## Connection

    RP2B ----- H/W UART --- RP2040 #1 --- PC1
       |
       +------ S/W UART --- RP2040 #2 --- PC2

    H/W UART TX (GPIO 14)  ---- RP2040 #1 RX (GPIO 1)
    S/W UART TX (GPIO 26)  ---- RP2040 #2 RX (GPIO 1)


## Requirements

  - Rapsberry PI (I use RP2 model B)
  - RP2040



