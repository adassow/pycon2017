import machine
import math

from ssd1306 import SSD1306_SPI, SSD1306_I2C
i2c = machine.I2C(
      scl=machine.Pin(5),
      sda=machine.Pin(4))
ssd = SSD1306_I2C(128, 64, i2c)
ssd.pixel(1,1,1)
ssd.show()