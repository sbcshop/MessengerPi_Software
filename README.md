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
    
#### Compatible speakers available Here:
* [2W 6 Ohm Mono Enclosed Speaker](https://shop.sb-components.co.uk/products/2-watt-6-ohm-mini-portable-speaker-for-small-electronic-projects-2pcs)
* [3 Watt 8 Ohm Mini Speaker](https://shop.sb-components.co.uk/products/3-watt-8-ohm-mini-speaker-full-range-portable-for-small-electronic-projects)
  
## Getting Started with MessengerPi
### Interfacing Details
- Pico and LoRa Interfacing
  | Pico | LoRa | Function |
  |---|---|---|
  |GP0 (UART0_TX) | Lo_RX | Serial UART communication pin |
  |GP1 (UART0_RX) | Lo_TX | Serial UART communication pin |

- Pico and Walkie-Talkie Interfacing
  | Pico | Walkie-Talkie | Function |
  |---|---|---|
  |GP4 (UART1_TX) | WT_RX | Serial UART communication pin |
  |GP5 (UART1_RX) | WT_TX  | Serial UART communication pin |
  |GP28 | H/L | Walkie-Talkie Power pin, for 0.5W/1W selection |
  
- Display interfacing details
  | Pico | Hardware Pin | Function |
  |---|---|---|
  |GP10 | SCLK  | Clock pin of SPI interface for display |
  |GP11 | DIN   | MOSI (Master OUT Slave IN) data pin of SPI interface|
  |GP12 | RESET | Display reset pin |
  |GP13 | CS    | Chip Select pin of SPI interface for display|
  |GP24 | D/C   | Data/command line of SPI interface for display |
  |GP26 | BL    | Backlight pin for display |

- SD Card interfacing : SPI0 of Pico is used for interfacing SDcard 
  | Pico | SDCard | Function |
  |---|---|---|
  |GP18 | SCK  | SPI clock pin |
  |GP19 | MOSI | SPI Master OUT Slave IN interface pin |
  |GP16 | MISO | SPI Master IN Slave OUT interface pin |
  |GP17 | CS   | Chip Select pin |
  
- QWERTY Keypad 6x6 Matrix
  | Pico | Function| 
  |---|---|
  | GP6, GP9, GP15, GP8, GP7, GP22 | Matrix Row Pins |
  | GP23, GP2, GP3, GP20, GP21, GP14 | Matrix Column Pins |

### 1. How to Install Boot Firmware in Pico of MessengerPi 

- Every board will be pre-installed with suitable MicroPython firmware with the inbuilt display driver module, so you can skip this and jump to [step 2](https://github.com/sbcshop/MessengerPi_Software/tree/main#2-running-first-code-in-messengerpi) for trying Demo Codes.
- In case, if you are required to reinstall **MicroPython firmware**. First, you need to *Press and Hold* the boot button on backside of MessengerPi, and then, without releasing the button, connect it to PC/laptop using Type C cable. Check below image for reference,
  
  <img src="https://github.com/sbcshop/MessengerPi_Software/blob/main/images/boot_btn.jpg" width="409" height="187">

- Now your device is in boot mode, and you will see a new mass storage device named "RPI-RP2" as shown in the below figure.

  <img src= "https://github.com/sbcshop/PiCoder-Software/blob/main/images/RPI_folder.jpg" width="720" height="360"/>

- Download the MicroPython firmware file provided in this repo above ["**_messengerPi_firmware.uf2_**"](https://github.com/sbcshop/MessengerPi_Software/blob/main/messengerPi_firmware.uf2). Drag and drop Firmware file onto the RPI-RP2 volume.

  <img src= "https://github.com/sbcshop/MessengerPi_Software/blob/main/images/messengerPi_firmware_upload.png" width="813" height="501">
  
### 2. Running First Code in MessengerPi
- For running application script we will use Thonny IDE, download from [here](https://thonny.org/) 

- Start Thonny IDE application, at bottom right corner, choose device with suitable com port
   <img src= "https://github.com/sbcshop/MessengerPi_Software/blob/main/images/comport_select.png" width="958" height="508"/>

- Download complete github which contains lib folder and examples. Upload [**lib**](https://github.com/sbcshop/MusicPi_Software/tree/main/Examples/lib) folder to Pico of MessengerPi

   <img src= "https://github.com/sbcshop/MessengerPi_Software/blob/main/images/upload_lib.png" width="958" height="508" />

- Now you can try running any example script code from github [here](https://github.com/sbcshop/MessengerPi_Software/tree/main/examples) or write your own codes to experiment. With script open in Thonny IDE and device connected, just click of green play button OR You can save file as _**main.py**_ into Pico for standalone execution without thonny.
   
   <img src= "https://github.com/sbcshop/MessengerPi_Software/blob/main/images/run_script.png" width="958" height="508"/>
   <img src= "https://github.com/sbcshop/MessengerPi_Software/blob/main/images/save_main.png" width="958" height="508"/>
   
<!--
#### Some Example Codes
   Try reference demo codes to test onboard components of MusicPi, make sure to move [**Lib files**](https://github.com/sbcshop/MusicPi_Software/tree/main/Examples/lib) into Pico before trying example codes. 
   - [Display Demo](https://github.com/sbcshop/MusicPi_Software/blob/main/Examples/Demo_Display.py) : code to test display
   - [RGB LED Demo](https://github.com/sbcshop/MusicPi_Software/blob/main/Examples/Demo_RGBLED.py) : code to blink or experiment with onboard RGB LEDs.
   - [Demo Audio I2S](https://github.com/sbcshop/MusicPi_Software/blob/main/Examples/Demo_Audio_I2S.py) : to play music using Pico/Pico W
   - [Play Songs](https://github.com/sbcshop/MusicPi_Software/blob/main/Examples/Demo_PlaySongs.py): store and play songs from SDcard with MusicPi, follow steps to create songs [below](https://github.com/sbcshop/MusicPi_Software/blob/main/README.md#build-songs-for-musicpi)
   
   Using this sample code as a guide, you can modify, build, and share codes!!
-->

## Configure onboard LoRa Module
 There are four operating modes, which are set by M1 and M0. Use onboard LoRa module slide switch for setting pin Logic 0 or 1. 
 
 <img src = "https://github.com/sbcshop/MessengerPi_Software/blob/main/images/LoRa_Mode_selection.jpg" width="169" height="187"/>
 
 |Operating Mode | M1 | M0 |
 |---|---|---|
 |Normal Mode | 0 | 0 |
 |WOR Mode | 0 | 1 |
 |Configuration Mode | 1 | 0 |
 |Deep Sleep Mode | 1 | 1 |


 For example, 
* **Normal Mode:** M1 = 0 & M0 = 0, so LoRa will be used with Pico of messengerPi for communication with other compatible LoRa device.

* **Config Mode:**
  - M1= 1 & M0 = 0, with this LoRa module is ready for configuration so you can change buadrate, operating frequency channel, etc.
  - For this remove jumper selection and interface LoRa module with USB-TTL converter.

    <img src = "https://github.com/sbcshop/MessengerPi_Software/blob/main/images/usb_ttl_lora_config.png" width="429" height="223" />

  - To perform configuration you can download [GUI application](https://github.com/sbcshop/USB_Type_C_to_LoRa_Dongle_Software/tree/main/GUI%20For%20Window) and follow steps mentioned on link [here](https://github.com/sbcshop/USB_Type_C_to_LoRa_Dongle_Software#lora-gui-for-configuration-run-with-the-help-of-gui).

## Configure Walkie-Talkie Module
- Walkie-Talkie module can be configure using code with pico itself, Make sure Walkie-Talkie side jumper selection is placed to maintain UART communication between Pico RP2040 and SA818S walkie-talkie module,

  <img src = "https://github.com/sbcshop/MessengerPi_Software/blob/main/images/walkie-talkie_selection.png" width="490" height="284" />
  
- Use code script for setup: [Walkie-Talkie Setting Example]()
- Adjust the commands as needed based on your testing requirements and the specific frequencies you want to use. Once you set frequency no need to run again this code for using Walkie-Talkie.
- During run time you will have to control GP28 pin of Pico for setting Walkie-Talkie power 0.5W/1W. By default if pin not used then wattage is 1.
  ```
  PWR_Sel = Pin(28, Pin.OUT)   # GP28 to control H/L pin of Walkie-Talkie for 0.5W/1W setting
  PWR_Sel.value(1)             # Logic High makes H/L pin LOW => 0.5Wattage SET, leave for 1W
  ``` 

  
## Resources
  * [Schematic](https://github.com/sbcshop/MessengerPi_Hardware/blob/main/Design%20Data/Messenger%20Pi%20sch.%20PDF.pdf)
  * [Hardware Files](https://github.com/sbcshop/MessengerPi_Hardware)
  * [Step File](https://github.com/sbcshop/MessengerPi_Hardware/blob/main/Mechanical%20Data/Messenger%20Pi%20.STEP)
  * [MicroPython getting started for RPi Pico/Pico W](https://docs.micropython.org/en/latest/rp2/quickref.html)
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
