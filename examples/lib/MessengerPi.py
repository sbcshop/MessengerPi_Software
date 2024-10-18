from machine import Pin,SPI
import machine
import utime
import st7789
import time

# key mappings 
keys_capital = (
        ( "Q", "W", "E", "R", "T","Y" ), 
        ( "U", "I", "O", "P","K", "J" ),
        ( "H", "G", "F","D", "S", "A" ),
        ( "V","B", "N", "M", "BKS", "L" ),
        ( "C", "X", "Z","SHIFT","CTRL"," " ),
        ( "UP","EXT","ENTER","LEFT","RIGHT","DOWN"))

keys_small = (
        ( "q", "w", "e", "r", "t","y" ), 
        ( "u", "i", "o", "p","k", "j" ),
        ( "h", "g", "f","d", "s", "a" ),
        ( "v","b", "n", "m", "bks", "l" ),
        ( "c", "x", "z","shift","ctrl"," " ),
        ( "up","ext","enter","left","right","down"))


keys_num_special = (
        ( "1", "2", "3", "4", "5","6" ), 
        ( "7", "8", "9", "0","-", ")" ),
        ( "(", "&", "%","#", "@", "!" ),
        ( "'",".", ",", "=", "bks", "+" ),
        ( "?", "/", "esc","shift","ctrl"," " ),
        ( "up","ext","enter","right","left","down"))

# define and configure pins as OUTPUT, INPUT
colPins = [23,2,3,20,21,14]  # GPIOs pin used for Column
rowPins = [6,9,15,8,7,22]	 # GPIOs pin used for Row

row = []    # list to hold row pin define
column = [] # list to hold row pin define

for item in rowPins:
    row.append(machine.Pin(item,machine.Pin.OUT))
for item in colPins:
    column.append(machine.Pin(item,machine.Pin.IN,machine.Pin.PULL_DOWN))

rlen = 6
clen = 6

def keyboard(keys_):
    global key
    for rowKey in range(rlen):
        row[rowKey].value(1)
        for colKey in range(clen):
            if column[colKey].value() == 1:
                key = keys_[rowKey][colKey]
                row[rowKey].value(0)
                time.sleep(0.2)
                return(key)
        row[rowKey].value(0)






