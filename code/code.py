import board
import time
from digitalio import DigitalInOut
import busio
import adafruit_dotstar as dotstar
from neopixel import NeoPixel
import supervisor
from adafruit_esp32spi import adafruit_esp32spi
import adafruit_esp32spi.adafruit_esp32spi_wifimanager as wifimanager
import adafruit_esp32spi.adafruit_esp32spi_wsgiserver as server
from secrets import secrets

class WebApp:

    def __init__( self, LED):
        self.INDEX = '/index.html'
        self.CHUNK_SIZE = 8912
        self.LED = LED

    def _serve_file( self, full_path):
        def resp_iter():
            with open( full_path, 'rb') as file:
                while True:
                    chunk = file.read( self.CHUNK_SIZE)
                    if chunk:
                        yield chunk
                    else:
                        break
        return resp_iter()

    def __call__( self, environ, start_response):
        method = environ['REQUEST_METHOD'].lower()
        path = environ['PATH_INFO'].split( '/')
        #print( method, path)
        if (method == 'get') and (path[1] == ''):
            resp_data = self._serve_file( self.INDEX)
            start_response( '200 OK', [('Content-Type', 'text/html')])
            return resp_data
        elif (method == 'put') and (path[1].lower() == 'light_on'):
            self.set_led( (255,100,0))
            start_response( '200 OK', [])
            return []
        elif (method == 'put') and (path[1].lower() == 'light_off'):
            self.set_led( (0,0,0))
            start_response( '200 OK', [])
            return []
        else:
            start_response( '200 OK', [])
            return []

    def set_led( self, clr):
        if hasattr(self.LED, "color"):
            self.LED.color = clr
        else:
            self.LED.fill(clr)

# turn off the microcontroller's onboard dotstar
uLED = dotstar.DotStar( board.APA102_SCK, board.APA102_MOSI, 1)
uLED.fill( (0,0,0))

# this is the LED that is actually visible outside the case
LED = NeoPixel( board.D5, 1, brightness=0.35, pixel_order='RGB')
LED.fill( (255,0,0))

esp_cs    = DigitalInOut( board.D10)
esp_ready = DigitalInOut( board.D9)
esp_reset = DigitalInOut( board.D7)
spi = busio.SPI( board.SCK, board.MOSI, board.MISO)
esp = adafruit_esp32spi.ESP_SPIcontrol( spi, esp_cs, esp_ready, esp_reset, debug=False)

wifi = wifimanager.ESPSPI_WiFiManager( esp, secrets)
print( 'connecting to wifi...')
wifi.connect()
print( 'find me here:', esp.pretty_ip( esp.ip_address))

app = WebApp(LED)
server.set_interface( esp)
wsgiServer = server.WSGIServer( 80, application=app)
wsgiServer.start()

for i in range(6):
    if i%2 == 0:
        LED.fill( (0,255,0))
    else:
        LED.fill(0)
    time.sleep( 0.1)

while True:
    try:
        wsgiServer.update_poll()
    except Exception as e:
        if 'Failed to send' not in str(e):
            print(e)
            supervisor.reload()
