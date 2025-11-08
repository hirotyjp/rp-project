import board
import digitalio
import time
import usb_hid
import neopixel
import busio

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)
uart = busio.UART(board.GP0, board.GP1, baudrate=115200, timeout=0.01)

DIGIT_KEY = {
    0x30: Keycode.ZERO,
    0x31: Keycode.ONE,
    0x32: Keycode.TWO,
    0x33: Keycode.THREE,
    0x34: Keycode.FOUR,
    0x35: Keycode.FIVE,
    0x36: Keycode.SIX,
    0x37: Keycode.SEVEN,
    0x38: Keycode.EIGHT,
    0x39: Keycode.NINE,
}

def send_num_key(ch):
    if ch in DIGIT_KEY:
        kbd.send(DIGIT_KEY[ch])

pixel_pin = board.GP16
num_pixels = 1

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=True)

for i in range(0,3):
    pixels[0] = (0, 0, 100)
    time.sleep(0.2)
    pixels[0] = (0, 0, 0) # OFF
    time.sleep(0.2)

while True:
    time.sleep(1)
    data = uart.read(32)
    if data:
        for b in data:
            if int(b) < 0x30 or int(b) > 0x39:
                pixels[0] = (55, 0, 0) # Red / Ascii
                time.sleep(0.2)
            else:
                pixels[0] = (0, 55, 0) # Green / Num key
                send_num_key(b)
                time.sleep(0.2)
            
            pixels[0] = (0, 0, 0)
            time.sleep(0.2)

        kbd.send(Keycode.ENTER)
