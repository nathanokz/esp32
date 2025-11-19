from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

i2c = I2C(0, scl=Pin(4), sda=Pin(5))
oled = SSD1306_I2C(128, 64, i2c)

def loading():
    for i in range(0,5):
        oled.text('loading.',24,28)
        oled.fill_rect(25,40,26,8,1)
        oled.show()
        time.sleep(0.3)
        oled.fill(0)
        
        oled.text('loading..',24,28)
        oled.fill_rect(25,40,51,8,1)
        oled.show()
        time.sleep(0.3)
        oled.fill(0)
        
        oled.text('loading...',24,28)
        oled.fill_rect(25,40,76,8,1)
        oled.show()
        time.sleep(0.3)
        oled.fill(0)

def enviar_dados():
    oled.text('enviando dados.',0,28)
    oled.show()
    time.sleep(0.5)
    oled.fill(0)
    
    oled.text('enviando dados..',0,28)
    oled.show()
    time.sleep(0.5)
    oled.fill(0)
    
    oled.text('enviando dados...',0,28)
    oled.show()
    time.sleep(0.5)
    oled.fill(0)
        
    for i in range(0,5):
        oled.text('esp32_client.ino',0,0)
        oled.text('{"type": "data",',0,10)
        oled.text('"from": "esp32",',0,20)
        oled.text('"payload":',0,30)
        oled.text('{"temp": 25.3,',0,40)
        oled.text('"hum": 60}}',0,50)
        oled.show()
        time.sleep(2)
        oled.fill(0)
        oled.show()
        time.sleep(2)
        
loading()
enviar_dados()


