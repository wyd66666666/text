import Adafruit_SSD1306
import time
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

OLED=Adafruit_SSD1306.SSD1306_128_32(rst=None,i2c_bus=0,gpio=1)

OLED.begin()

OLED.clear()
OLED.display()
time.sleep(1)

font=imageFont.load_default()

width=OLED.width
height=OLED.height
image=Image.new("1",(width,height))

while True:
    Draw=ImageDraw.Draw(image)
    Draw.rectangle((0,0,width,height),outline=0,fill=0)
    Draw.text((0,0),"OLED TEXTING",font=font,fill=255)

    OLED.image(image)
    OLED.display()
    time.sleep(1)

