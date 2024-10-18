# Code to configure and test Walkie-Talkie module using onboard Pico RP2040
'''
This code will help you test various functionalities of the SA818S-CE audio module by
sending different AT commands and reading their responses. Adjust the commands as needed
based on your testing requirements and the specific frequencies you want to use.

Make sure Walkie-Talkie side jumper selection is placed to maintain UART communication
between Pico RP2040 and SA818S walkie-talkie module

Example shows how to check RSSI, Set/Read frequency, Set volume of Walkie-Talkie

Commands:
AT+DMOSETGROUP: Sets the frequency, CTCSS, CDCSS, squelch, etc.
AT+DMOSETVOLUME: Sets the volume level.
AT+SETFILTER: Sets the pre-emphasis, high-pass, and low-pass filters.
AT+DMOREADGROUP: Reads the current group settings.
AT+DMOCONNECT: Verifies the module connection.
AT+VERSION: Reads the module version.
AT+SETTAIL: Sets the tail tone on or off.

Uncomment respective commands provided below to test and configure.
Once Walkie-talkie configure no need to repeat this code as setting remains when powered again.

Disclaimer:
License-free radio for US 467.5625 to 467.7125, with 0.5 watts

For UK range from 446.0062 to 446.1937, total 16 channel the channel raster is 12.5 kHz,
the maximum transmission power is 0.5 watts and a transmission cycle must not last longer than 180 seconds.

Recommended to consult local radio engineer to confirm License-free usage requirement for your Region.

'''
from machine import UART, Pin
import st7789
import time
import vga1_bold_16x32 as font

# Initialize UART
uart = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))

PWR_Sel = Pin(28, Pin.OUT)   # GP28 to control H/L pin of Walkie-Talkie for 0.5W/1W setting
PWR_Sel.value(1)             # Logic High makes H/L pin LOW => 0.5Wattage SET, leave for 1W


# Function to send commands to the SA818S-CE module
def send_command(command):
    uart.write(command + '\r\n')
    time.sleep(1)
    response = uart.readline()
    print(response)
    time.sleep(0.1)


# Example commands
send_command('RSSI?')

# Set frequency group (example frequencies for UK and US)
send_command('AT+DMOSETGROUP=0,446.0812,446.0812,0000,1,0000')  # UK frequency
# send_command('AT+DMOSETGROUP=0,467.7125,467.7125,0000,1,0000')  # US frequency

# Read group parameters
send_command('AT+DMOREADGROUP')

# Set volume level (1 to 8)
send_command('AT+DMOSETVOLUME=5')

'''
# Set filter (pre-emphasis, high-pass, low-pass)
send_command('AT+SETFILTER=1,0,0')

# Read group parameters
send_command('AT+DMOREADGROUP')

# Check connection
send_command('AT+DMOCONNECT')

# Set version (read the version of the module)
send_command('AT+VERSION')

# Set the tail tone (0 = off, 1 = on)
send_command('AT+SETTAIL=0')

'''