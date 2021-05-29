# IoTDnD
an internet-of-things Do Not Disturb light

# What/Why
This is a small WiFi device that hangs out on your network and serves up a web interface to your browser. You use the web interface to turn a light on the device on and off.

This one was a request from a friend. He and his roommate were both working from home, and they wanted to be able to quickly and easily let each other know when one was on a work call. I initially suggested using a text message, but eventually I sent them two of these little boxes:

<img width=17% src='https://github.com/probablyfine/IoTDnD/raw/main/photos/open-under2.jpg'> <img width=17% src='https://github.com/probablyfine/IoTDnD/raw/main/photos/IMG_6161.jpg'> <img width=17% src='https://github.com/probablyfine/IoTDnD/raw/main/photos/top-unlit.jpg'> <img width=17% src='https://github.com/probablyfine/IoTDnD/raw/main/photos/top-lit.jpg'> <img width=17% src='https://github.com/probablyfine/IoTDnD/raw/main/photos/bottom.jpg'>

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
I laid out the PCB in the free version of [EAGLE](https://en.wikipedia.org/wiki/EAGLE_(program)). There are very good arguments for using [KiCad](https://en.wikipedia.org/wiki/KiCad) instead, but EAGLE is what I know. Plus, it's what Adafruit uses, which means I was able to import their board files and use the two modules' footprints for my layout. 

The PCB is very simple. There are places to mount the microcontroller and the WiFi module, the RGB LED, and two capacitors (I only ended up having room for one in the enclosure). There's a mounting hole that lines up with the enclosure's internal screw hole, and cutouts to make room for the screw holes for the enclosure's cover.

The copper traces are pretty minimal, too. There are a few power connections, some connections between the microcontroller and WiFi module, and a data line from the microcontroller to the RGB LED.

Getting professional-quality PCBs made is insanely easy and inexpensive these days. I normally use [OSH Park](https://oshpark.com/) and highly recommend them. For this project, I wanted to try out [JLCPCB](https://jlcpcb.com/), and had a good experience with them as well. One nice feature of OSH Park's service is that you can drop an [EAGLE .brd file](https://github.com/probablyfine/IoTDnD/blob/main/pcb/IoTDnD.brd) directly onto their landing page without generating [Gerber files](https://en.wikipedia.org/wiki/Gerber_format) first.

<img width=13% src='https://github.com/probablyfine/IoTDnD/raw/main/photos/EAGLE-brd.png'> <img width=13% src='https://github.com/probablyfine/IoTDnD/raw/main/photos/JLCPCB-top.png'> <img width=13% src='https://github.com/probablyfine/IoTDnD/raw/main/photos/JLCPCB-bottom.png'> <img width=20% src='https://github.com/probablyfine/IoTDnD/raw/main/photos/IMG_6150.jpg'> <img width=20% src='https://github.com/probablyfine/IoTDnD/raw/main/photos/IMG_6151.jpg'>

With everything soldered, I used a Dremel tool to bore out a hole in the enclosure for the LED and a cutout for the USB port for power.

<img width=15% src='https://github.com/probablyfine/IoTDnD/raw/main/photos/IMG_6157.jpg'> <img width=15% src='https://github.com/probablyfine/IoTDnD/raw/main/photos/IMG_6162.jpg'> <img width=15% src='https://github.com/probablyfine/IoTDnD/raw/main/photos/open-over.jpg'> <img width=15% src='https://github.com/probablyfine/IoTDnD/raw/main/photos/open-under1.jpg'> 

#### 
## Software
The microcontroller I'm using runs [CircuitPython](https://circuitpython.org/), which makes it possible to do some pretty powerful things with very little code. Adafruit also provides a ton of libraries and examples; I based the web server functionality in my code on [this example](https://github.com/adafruit/Adafruit_CircuitPython_ESP32SPI/blob/master/examples/server/esp32spi_wsgiserver.py) they provide.

The [code](https://github.com/probablyfine/IoTDnD/blob/main/code/code.py) does a few things:
- sets up an SPI connection with the WiFi module
- connects to a WiFi network (2.4 GHz only) using the specified [SSID and password](https://github.com/probablyfine/IoTDnD/blob/main/code/secrets.py)
- Polls the WiFi module for incoming [HTTP requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)

It responds to a GET request to its root IP address by returning an [HTML file](https://github.com/probablyfine/IoTDnD/blob/main/code/index.html). It also reponds to PUT requests to '/light_on' and '/light_off' by turning the LED on or off.

You can see how the browser renders the HTML file in the image towards the top of this document. That file is a heavily modified version of [this example code](https://github.com/cyborg5/IRLib2/blob/master/IRLib2/examples/Iot_IR/adafruit_remote.html) that Chris Young did for Adafruit. Basically, it renders two buttons and a small status indicator (the little octopus in the upper left of the screenshot above). Tapping either of the two buttons generates the appropriate PUT request, which is received by the WiFi module and microcontroller.

If you're trying this out, you need to modify [this line](https://github.com/probablyfine/IoTDnD/blob/7540f51e6421b3274a6c39247116161634d67c39/code/index.html#L48) in the HTML document to match the IP address of the WiFi module. If this is a permanent installation, you'll want to configure your router to assign the module a static IP address so you don't have to update the HTML file on re-connects.

