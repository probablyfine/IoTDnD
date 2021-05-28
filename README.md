# IoTDnD
an internet-of-things Do Not Disturb light

# What/Why
This is a small WiFi device that hangs out on your network and serves up a web interface to your browser. You use the web interface to turn a light on the device on and off.

This one was a request from a friend. He and his roommate were both working from home, and they wanted to be able to quickly and easily let each other know when one was on a work call. I sent them two of these little boxes.

<img width=20% src='https://github.com/probablyfine/IoTDnD/blob/main/photos/open-under2.jpg'> <img width=20% src='https://github.com/probablyfine/IoTDnD/raw/main/photos/IMG_6161.jpg'> <img width=20% src='https://github.com/probablyfine/IoTDnD/raw/main/photos/IMG_6162.jpg'> <img width=20% src='https://github.com/probablyfine/IoTDnD/raw/main/photos/IMG_6163.jpg'>

Tap the sun for on, tap the moon for off.

<img width=45% src='https://github.com/probablyfine/IoTDnD/raw/main/photos/web.png'>

# How
There are a few parts to this project.
- An [ESP32](https://en.wikipedia.org/wiki/ESP32)-based [module from Adafruit](https://www.adafruit.com/product/4201), which handles the WiFi functions
- An [M4](https://en.wikipedia.org/wiki/ARM_Cortex-M)-based [microcontroller board from Adafruit](https://www.adafruit.com/product/3800), which controls the WiFi module over [SPI](https://en.wikipedia.org/wiki/Serial_Peripheral_Interface), and controls the device's LED
- A [custom-made](https://github.com/probablyfine/IoTDnD/raw/main/photos/EAGLE-brd.png) [PCB](https://github.com/probablyfine/IoTDnD/raw/main/photos/IMG_6150.jpg) that connects the microcontroller to the WiFi module and to the LED, and provides a way to mount everything in box
- Some [Python code](https://github.com/probablyfine/IoTDnD/blob/main/code/code.py) that runs a web server on the microcontroller
- A [web-based interface](https://github.com/probablyfine/IoTDnD/blob/main/code/index.html) that the microcontroller sends to your browser via the WiFi module

# Details
## Hardware

## Software
