# MessengerPi_Software
<img src="https://github.com/sbcshop/MessengerPi_Software/blob/main/images/MessengerPi%20banner.png">

Powered by the Raspberry Pi Pico RP2040, MessengerPi combines walkie-talkie and LoRa modules for versatile wireless communication. Ideal for hikers, campers, and makers, MessengerPi ensures reliable communication for adventures, emergencies, and areas with poor mobile coverage. Stay connected wherever your journey takes you with MessengerPi.

This github provides getting started instructions for MessengerPi.

### Features:
- Powered by Raspberry Pi Pico RP2040, a dual-core Arm Cortex-M0+ CPU with a maximum speed of 133 MHz and a 2.0" TFT display for visual engagement.
- Type C interface for power and programming.
- Equipped with a walkie-talkie and a LoRa module for wireless communication
- LoRa module is used for low data rate communication, such as sending simple messages.
- Qwerty keypad to easily type messages for sending.
- LoRa can attain distances up to 5 kilometers for message transmission in open air.
- Choose from license-free ISM bands of 433MHz, 868MHz, and 915MHz for LoRa.
- Walkie-Talkies can transmit audio up to 1km in open air.
- Walkie-Talkie frequencies can be tuned between 400-470MHz with wattage settings (0.5W and 1W) to meet regulations for license-free usage in different regions.
- Easily communicate with individuals at a distance via walkie-talkie utilizing the onboard microphone.
- Push to Talk button for easy switch between Audio transmission and receive mode
- Multiple audio output choices are provided, including a 2mm JST connector and a 2.54" 2 pin header for connecting 3W speakers.
- There is also a 3.5mm Aux OUT to attach headphones for private listening.
- Easy data logging with onboard micro SD card compatibility and status LEDs for board power, LoRa, and walkie-talkie transmission.
- UART breakout of LoRa and Walkie-talkie module is offered for custom setup as needed.

### Specifications:
- **Microcontroller:** RP2040
- **Supply Voltage:** 5V Type C 
- **Operating pin voltage:** 3.3V
- **Battery Connector:** 3.7V Lithium Ion
- **Display:** 
	- Display Size: 2.0”
	- Display Type: IPS TFT 
	- Display Resolution:  240×320 pixels
	- Display colors: 65K
	- Luminance(cd/m2): 350
	- Display interface: SPI
	- Display Driver: ST7789V 
- **Audio Outputs:**
	- 3W Speaker Output at 2.54” standard Header and 2mm JST 
	- Standard 3.5mm TRS Headphone Jack
- **Walkie-Talkie Module :**
	- Frequency Range => 400 ~ 470MHz
	- Bandwidth => 12.5KHz / 25 KHz
	- Communication Distance => around 1km tested in Open area
	- Current Consumption => Rx around 60 mA and for Tx around 750 mA
- **LoRa Module :**
	- communication distance => up to 5km in open area
	- Maximum transmission power => 60mW, software multi-level adjustable
	- Support the license-free ISM => 433MHz, 868MHz, 915MHz band
	- Support air date rate => 0.3kbps ~ 62.5kbps 
- Operating Temperature Range: -20°C ~ +70°C 

## Hardware Overview of MessengerPi
### Pinout
<img src="https://github.com/sbcshop/MessengerPi_Software/blob/main/images/MessengerPi%20Pinout.png">

<!--
- **<ins>Walkie-Talkie Module</ins>**: SA818S-CE walkie-talkie module for high data audio communications.
- **<ins>LoRa Module</ins>**: LoRa module which handle low data message communications.
- **<ins>Control Switch/Buttons<ins>** : Onboard there are three control switch,
   - ** PD Slide Switch** : Use to switch ON/OFF Walkie-talkie module power. On **+ve** side Walkie-talkie module is **ON** while **-ve** side turn module **OFF**.
   - ** Push-To-Talk** : Push switch when pressed walkie-talkie is in audio transmission mode, so talk to send audio. When release it is in reception mode to listen incoming audio from other walkie-talkie, status indicated by LED.

- **<ins>Type C Interface</ins>**: Type C interface for power and programming Pico RP2040 MCU.
- **<ins>External Power</ins>**: Additional power source option as 2mm JST to connect 3.7V lithium ion battery for portable use. Onboard charging facility available.
- **<ins>Audio Output</ins>**: Three options to listen incoming audio,
  - Use 2mm JST connector or 2.54" standard header to connect 2W or 3W speaker. Checkout below for compatible speaker options.
  - For private listening use 3.5mm Audio Jack. Required 3 Pole TRS Aux pin connector for Compatibility.
-->
#### Compatible speakers available Here:
* [2W 6 Ohm Mono Enclosed Speaker](https://shop.sb-components.co.uk/products/2-watt-6-ohm-mini-portable-speaker-for-small-electronic-projects-2pcs)
* [3 Watt 8 Ohm Mini Speaker](https://shop.sb-components.co.uk/products/3-watt-8-ohm-mini-speaker-full-range-portable-for-small-electronic-projects)
  
## Getting Started with MessengerPi

## Resources
  * [Schematic](https://github.com/sbcshop/MessengerPi_Hardware/blob/main/Design%20Data/Messenger%20Pi%20sch.%20PDF.pdf)
  * [Hardware Files](https://github.com/sbcshop/MessengerPi_Hardware)
  * [Step File](https://github.com/sbcshop/MessengerPi_Hardware/blob/main/Mechanical%20Data/Messenger%20Pi%20.STEP)
  * [RP2040 Datasheet](https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf)
  * [LoRa Module Manual]()
  * [Walkie-Talkie Module Manual](https://github.com/sbcshop/MessengerPi_Software/blob/main/documents/SA818S-U_Datasheet.pdf)


## Related Products

  * [GatePi - Pico and LoRa based 4Channel Relay](https://shop.sb-components.co.uk/products/gatepi?_pos=3&_sid=276907aab&_ss=r)
  
    ![GatePi](https://shop.sb-components.co.uk/cdn/shop/products/gate-pi-photoi.png?v=1647335212&width=300)
  
  * [USB-to-LoRa dongle](https://shop.sb-components.co.uk/products/usb-to-lora-dongle?_pos=1&_sid=276907aab&_ss=r)
  
    ![USB-to-LoRa dongle](https://shop.sb-components.co.uk/cdn/shop/products/05_2.png?v=1678712489&width=300)
  
  * [Pico LoRa Expansion](https://shop.sb-components.co.uk/products/pico-lora-expansion?_pos=6&_sid=276907aab&_ss=r) 
  
    ![Pico LoRa Expansion](https://shop.sb-components.co.uk/cdn/shop/products/loar-2_1.jpg?v=1670922482&width=300)

  * [Lo-Fi : ESP based LoRa for Long Range communication](https://shop.sb-components.co.uk/products/lo-fi?_pos=22&_sid=276907aab&_ss=r) 
  
    ![Lo-Fi](https://shop.sb-components.co.uk/cdn/shop/files/SHOPSIZE3.jpg?v=1700211751&width=300)
    

 
## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=300">
</p>
