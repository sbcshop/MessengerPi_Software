from machine import Pin, SPI, UART
import MessengerPi
#from MessengerPi import *
import time
import st7789
import sdcard
import os
import vga1_16x32 as font
import vga1_8x16 as font1
import vga1_16x16 as font2
import vga2_8x8 as font3

# Initialize SPI and display
spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))
tft = st7789.ST7789(spi, 320, 240, reset=Pin(12, Pin.OUT), cs=Pin(13, Pin.OUT), dc=Pin(24, Pin.OUT), backlight=Pin(26, Pin.OUT), rotation=1)

# Initial values
Keys = [MessengerPi.keys_capital, MessengerPi.keys_small, MessengerPi.keys_num_special]
key_sel = 0
Keys_current = Keys[key_sel]
choice = ["ABC", "abc", "123"][key_sel]

# Fonts
fonts = [(font, 16, 32), (font1, 8, 16), (font2, 16, 16), (font3, 8, 8)]
font_sel = 0  # Manually set the starting font index (0, 1, 2, or 3)
current_font, font_width, font_height = fonts[font_sel]

# Text buffer and cursor position
text = [[" "]*32 for _ in range(15)]
cursor_x, cursor_y = 0, 2

# Initial display message
tft.fill(0)
tft.text(current_font, "Press Key!     " + "ABC", 0, 10, st7789.GREEN)

lora_uart = UART(0,baudrate = 9600,tx = Pin(0),rx = Pin(1))

lora_uart.write("MessengerPi Ready!\n")#send data


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
    #tft.text(current_font, "Press Key!", 0, 10, st7789.GREEN)
    tft.text(current_font, "Press Key!     " + choice, 0, 10, st7789.GREEN)
    draw_cursor(cursor_x, cursor_y)

ctrl_keys = ["bks","shift","ctrl","up","ext","enter","left","right","down"]
msg_lst = []

while True:
    draw_cursor(cursor_x, cursor_y)
    key = MessengerPi.keyboard(Keys_current)
    
    data_Read = lora_uart.readline() #read data comming from other MessengerPi or compatible LoRa device
    #print(data_Read)
    
    if data_Read is not None:
        tft.text(font1, "Received: " + str(data_Read.decode()), 30, 220, st7789.YELLOW)
        print(data_Read)
        time.sleep(1)
        tft.text(font1, "Received: " + str(data_Read.decode()), 30, 220, st7789.BLACK)
        
    if key is not None:
        clear_cursor(cursor_x, cursor_y)
        if key.lower() not in ctrl_keys:
            msg_lst.append(key)
            #print("msg list ", msg_lst)
        
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
                
            message = "".join(msg_lst)
            print("Sending ", message)
            lora_uart.write(message)#send data
            msg_lst.clear()

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
            tft.text(current_font, "Send Msg:", 0, 10, st7789.GREEN)
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


