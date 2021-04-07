from m5stack import *
from m5stack_ui import *
from uiflow import *
import time
from m5stack import touch

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)


prev_brightness = None
interval = None
brightness = None
prevmillis = None
currentmillis = None


slider0 = M5Slider(x=45, y=150, w=200, h=12, min=0, max=100, bg_c=0xa0a0a0, color=0x08A2B0, parent=None)
screensaver_time = M5Label('xx', x=139, y=73, color=0x000, font=FONT_MONT_14, parent=None)
ss_time_dec = M5Btn(text='-', x=44, y=66, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
ss_time_inc = M5Btn(text='+', x=187, y=68, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)

from numbers import Number



def slider0_changed(prev_brightness):
  global interval, brightness, prevmillis, currentmillis
  screen.set_screen_brightness((slider0.get_value()))
  brightness = slider0.get_value()
  slider0.set_value(brightness)
  pass
slider0.changed(slider0_changed)

def ss_time_inc_pressed():
  global interval, prev_brightness, brightness, prevmillis, currentmillis
  interval = (interval if isinstance(interval, Number) else 0) + 1000
  slider0.set_value(brightness)
  screen.set_screen_brightness((slider0.get_value()))
  pass
ss_time_inc.pressed(ss_time_inc_pressed)

def ss_time_dec_pressed():
  global interval, prev_brightness, brightness, prevmillis, currentmillis
  interval = (interval if isinstance(interval, Number) else 0) + -1000
  slider0.set_value(brightness)
  screen.set_screen_brightness((slider0.get_value()))
  pass
ss_time_dec.pressed(ss_time_dec_pressed)


prev_brightness = 100
prevmillis = 0
brightness = 100
interval = 5000
slider0.set_value(100)
while True:
  currentmillis = time.ticks_ms()
  if (touch.status()) == 1:
    prevmillis = currentmillis
    screen.set_screen_brightness((slider0.get_value()))
    slider0.set_value(brightness)
  if currentmillis - prevmillis >= interval:
    prevmillis = currentmillis
    if (touch.status()) == 0:
      screen.set_screen_brightness(10)
      slider0.set_value(10)
  if interval <= 5000:
    interval = 5000
  if interval >= 60000:
    interval = 60000
  screensaver_time.set_text(str(interval))
  wait_ms(2)
