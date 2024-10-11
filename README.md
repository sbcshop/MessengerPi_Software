# MessengerPi_Software

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
