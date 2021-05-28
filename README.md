# IoTDnD
an internet-of-things Do Not Disturb light

# What/Why
This is a small WiFi device that hangs out on your network and serves up a web interface to your browser. You use the web interface to turn a light on the device on and off.

This one was a request from a friend. He and his roommate were both working from home, and they wanted to be able to quickly and easily let each other know when one was on a work call. I sent them two of these little boxes.

<img width=15% src='https://github.com/probablyfine/IoTDnD/raw/main/photos/open-under2.jpg'> <img width=15% src='https://github.com/probablyfine/IoTDnD/raw/main/photos/IMG_6161.jpg'> <img width=15% src='https://github.com/probablyfine/IoTDnD/raw/main/photos/top-unlit.jpg'> <img width=15% src='https://github.com/probablyfine/IoTDnD/raw/main/photos/top-lit.jpg'> <img width=15% src='https://github.com/probablyfine/IoTDnD/raw/main/photos/bottom.jpg'>

Tap the sun for on, tap the moon for off.

<img width=45% src='https://github.com/probablyfine/IoTDnD/raw/main/photos/web.png'>

# How
There are a few parts to this project.
- An [ESP32](https://en.wikipedia.org/wiki/ESP32)-based [module from Adafruit](https://www.adafruit.com/product/4201), which handles the WiFi functions
- An [M4](https://en.wikipedia.org/wiki/ARM_Cortex-M)-based [microcontroller board from Adafruit](https://www.adafruit.com/product/3800), which controls the WiFi module over [SPI](https://en.wikipedia.org/wiki/Serial_Peripheral_Interface), and controls the device's LED
- A [custom-made](https://github.com/probablyfine/IoTDnD/raw/main/photos/EAGLE-brd.png) [PCB](https://github.com/probablyfine/IoTDnD/raw/main/photos/IMG_6150.jpg) that connects the microcontroller to the WiFi module and to the LED, and provides a way to mount everything in a box
- Some [Python code](https://github.com/probablyfine/IoTDnD/blob/main/code/code.py) that runs a web server on the microcontroller
- A [web-based interface](https://github.com/probablyfine/IoTDnD/blob/main/code/index.html) that the microcontroller sends to your browser via the WiFi module

# Details
## Hardware
### Smart parts
The critical components are the [microcontroller](https://www.adafruit.com/product/3800) and the [WiFi module](https://www.adafruit.com/product/4201). There are plenty of similar solutions out there, but this pairing works very well. If you're putting this together yourself, you probably want [this board](https://www.adafruit.com/product/4000) from Adafruit instead, which has both of these products built onto it-- no need to worry about soldering anything. I wanted to use a particular [enclosure](https://www.aliexpress.com/item/32782067140.html) that was too small for the single-board option, and I liked having an excuse to make a PCB, so I got the two components separately. If you go that route there's good [documentation](https://learn.adafruit.com/adafruit-airlift-breakout/overview) from Adafruit.

The last important part is the LED. Both of the Adafruit microcontroller boards I linked have on-board RGB LEDs, which are very bright and totally usable. I used these [nice 5mm ones](https://www.pololu.com/product/2535) from Pololu instead-- they have a diffused lens, which is easier on the eyes, and the form-factor makes it easy to display outside the enclosure.

### Dumb parts
#### PCB
I laid out the PCB in the free version of [EAGLE](https://en.wikipedia.org/wiki/EAGLE_(program)). There are very good arguments for using [KiCad](https://en.wikipedia.org/wiki/KiCad) instead, but EAGLE is what I know. Plus, it's what Adafruit uses, which means I was able to import their board files and use the two modules' footprints for my layout. 

The PCB is very simple. There are places to mount the microcontroller and the WiFi module, the RGB LED, and two capacitors (I only ended up having room for one in the enclosure). There's a mounting hole that lines up with the enclosure's internal screw hole, and cutouts to make room for the screw holes for the enclosure's cover.

The copper traces are pretty minimal, too. There are a few power connections, some connections between the microcontroller and WiFi module, and a data line from the microcontroller to the RGB LED.

Getting small professional-quality PCBs made is insanely easy and inexpensive these days. I normally use [OSH Park](https://oshpark.com/) and highly recommend them. For this project, I wanted to try out [JLCPCB](https://jlcpcb.com/), and had a good experience with them as well. One nice feature of OSH Park's service is that you can drop an [EAGLE .brd file](https://github.com/probablyfine/IoTDnD/raw/main/pcb/IoTDnD.brd) directly onto their landing page without generating [Gerber files](https://en.wikipedia.org/wiki/Gerber_format) first.
<img width=25% src='

## Software
