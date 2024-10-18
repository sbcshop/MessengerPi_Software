''' Send and Receive communication demo using LoRa Module '''

from machine import Pin,UART
import time
 
lora_uart = UART(0,baudrate = 9600,tx = Pin(0),rx = Pin(1))

lora_uart.write("Hello from MessengerPi\n")#send data

while 1:
    data_Read = lora_uart.readline() #read data comming from other MessengerPi or compatible LoRa device
    #print(data_Read)
    
    if data_Read is not None:
        print(data_Read)
        lora_uart.write("Received\n")#send data
          
    time.sleep(0.1)



