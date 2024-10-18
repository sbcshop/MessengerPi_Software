''' Demo code for onboard TFT Display '''
from machine import Pin, SPI, UART
import time
import st7789
import sdcard
import os
import vga1_16x32 as font
import vga1_8x16 as font1
import vga1_16x16 as font2
import vga2_8x8 as font3

spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))
tft = st7789.ST7789(spi, 240, 320, reset=Pin(12, Pin.OUT), cs=Pin(13, Pin.OUT), dc=Pin(24, Pin.OUT), backlight=Pin(26, Pin.OUT), rotation=1)

def intro_animation():
    tft.fill(0) # Clear screen
    i_1 = 320
    j_1 = 240
    for x in range(0, 240, 30):
        for y in range(0, 320, 30):
            tft.rect(x, y, 30, 30, st7789.CYAN)
            time.sleep(0.05)
    tft.fill(0) # Clear screen

def display_intro_message():
    tft.fill(0)  # Clear screen
    
    messages = [
        ("Welcome to", 30, 30, st7789.YELLOW),
        ("MessengerPi", 20, 70, st7789.CYAN),
        ("Your Ultimate", 20, 120, st7789.GREEN),
        ("LoRa &", 80, 160, st7789.RED),
        ("Walkie Talkie", 20, 200, st7789.MAGENTA)
    ]
    
    for text, x, y, color in messages:
        tft.text(font, text, x, y, color)
    
    time.sleep(5)
    tft.fill(0)  # Clear screen

def display_logo():
    tft.fill(0) # Clear screen
    tft.jpg("/lib/sb_logo.jpg", 0, 0, st7789.FAST)
    time.sleep(2)
    tft.fill(0) # Clear screen

def main():
    tft.init()
    tft.fill(0) # Clear screen
    tft.text(font1, "Hello...", 20, 5, st7789.WHITE)
    time.sleep(1)

    # Display the logo
    display_logo()

    # Show intro animation
    intro_animation()

    # Display intro message
    display_intro_message()

    # Final message
    tft.fill(0) # Clear screen
    tft.text(font1, "Enjoy your", 60, 100, st7789.GREEN)
    tft.text(font1, "MessengerPi!", 40, 140, st7789.GREEN)
    time.sleep(5)
    tft.fill(0) # Clear screen

# Run the main function
main()

