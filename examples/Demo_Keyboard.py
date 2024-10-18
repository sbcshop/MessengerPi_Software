from machine import Pin, SPI
import MessengerPi
from MessengerPi import *
import time
import st7789
import sdcard
import os
import vga1_16x32 as font
import vga1_8x16 as font1
import vga1_16x16 as font2
import vga2_8x8 as font3

# Initialize SPI and display
spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11), miso=Pin(12))
tft = st7789.ST7789(spi, 320, 240, reset=Pin(12, Pin.OUT), cs=Pin(13, Pin.OUT), dc=Pin(24, Pin.OUT), backlight=Pin(26, Pin.OUT), rotation=1)

# Initial values
Keys = [keys_capital, keys_small, keys_num_special]
key_sel = 0
Keys_current = Keys[key_sel]

# Fonts
fonts = [(font, 16, 32), (font1, 8, 16), (font2, 16, 16), (font3, 8, 8)]
font_sel = 0  # Manually set the starting font index (0, 1, 2, or 3)
current_font, font_width, font_height = fonts[font_sel]

# Text buffer and cursor position
text = [[" "]*32 for _ in range(15)]
cursor_x, cursor_y = 0, 2

# Initial display message
tft.fill(0)
tft.text(current_font, "Press Key!", 0, 10, st7789.GREEN)

def draw_cursor(x, y):
    tft.rect(x * font_width, y * font_height, font_width, font_height, st7789.WHITE)

def clear_cursor(x, y):
    tft.rect(x * font_width, y * font_height, font_width, font_height, st7789.BLACK)
    tft.text(current_font, text[y][x], x * font_width, y * font_height, st7789.YELLOW)

def update_display():
    tft.fill(0)
    for y, row in enumerate(text):
        for x, char in enumerate(row):
            tft.text(current_font, char, x * font_width, y * font_height, st7789.YELLOW)
    tft.text(current_font, "Press Key!", 0, 10, st7789.GREEN)
    draw_cursor(cursor_x, cursor_y)

while True:
    draw_cursor(cursor_x, cursor_y)
    key = MessengerPi.keyboard(Keys_current)

    if key is not None:
        clear_cursor(cursor_x, cursor_y)
        
        if key.lower() == "shift":
            key_sel = (key_sel + 1) % 3
            Keys_current = Keys[key_sel]
            choice = ["ABC", "abc", "123"][key_sel]
            tft.text(current_font, "Press Key!     " + choice, 0, 10, st7789.GREEN)
            print(f"Switched to: {choice}")

        elif key.lower() == "ctrl":
            font_sel = (font_sel + 1) % len(fonts)
            current_font, font_width, font_height = fonts[font_sel]
            update_display()
            print(f"Font switched to: {font_sel}")

        elif key.lower() == "enter":
            cursor_y += 1
            cursor_x = 0
            if cursor_y >= 240 // font_height:
                cursor_y = 2

        elif key.lower() == "space":
            text[cursor_y][cursor_x] = " "
            cursor_x += 1
            if cursor_x >= 320 // font_width:
                cursor_x = 0
                cursor_y += 1
                if cursor_y >= 240 // font_height:
                    cursor_y = 2

        elif key.lower() == "bks":
            if cursor_x > 0:
                cursor_x -= 1
            elif cursor_y > 2:
                cursor_y -= 1
                cursor_x = (320 // font_width) - 1
            text[cursor_y][cursor_x] = " "
            clear_cursor(cursor_x, cursor_y)  # Clear the previous character display
        
        elif key.lower() == "up":
            if cursor_y > 2:
                cursor_y -= 1

        elif key.lower() == "down":
            if cursor_y < (240 // font_height) - 1:
                cursor_y += 1

        elif key.lower() == "left":
            if cursor_x > 0:
                cursor_x -= 1
            elif cursor_y > 2:
                cursor_y -= 1
                cursor_x = (320 // font_width) - 1

        elif key.lower() == "right":
            if cursor_x < (320 // font_width) - 1:
                cursor_x += 1
            elif cursor_y < (240 // font_height) - 1:
                cursor_x = 0
                cursor_y += 1

        elif key.lower() == "ext":
            tft.fill(0)
            tft.text(current_font, "Press Key!", 0, 10, st7789.GREEN)
            cursor_x, cursor_y = 0, 2
            text = [[" "]*32 for _ in range(15)]

        else:
            text[cursor_y][cursor_x] = key
            tft.text(current_font, key, cursor_x * font_width, cursor_y * font_height, st7789.YELLOW)
            cursor_x += 1
            if cursor_x >= 320 // font_width:
                cursor_x = 0
                cursor_y += 1
                if cursor_y >= 240 // font_height:
                    cursor_y = 2

        draw_cursor(cursor_x, cursor_y)
        
    time.sleep(0.1)

