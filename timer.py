from m5stack import *
from m5stack_ui import *
from uiflow import *
import time

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)

count = None
seconds = None
hours = None
minutes = None
vibration_count = None

h = M5Label('00', x=63, y=67, color=0x000, font=FONT_MONT_48, parent=None)
m = M5Label('00', x=128, y=67, color=0x000, font=FONT_MONT_48, parent=None)
s = M5Label('00', x=197, y=67, color=0x000, font=FONT_MONT_48, parent=None)
h_add = M5Btn(text='+', x=59, y=10, w=50, h=50, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
h_reduce = M5Btn(text='-', x=63, y=111, w=50, h=50, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
m_add = M5Btn(text='+', x=124, y=10, w=50, h=50, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
s_add = M5Btn(text='+', x=197, y=10, w=50, h=50, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
m_red = M5Btn(text='-', x=136, y=119, w=50, h=50, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
s_red = M5Btn(text='-', x=213, y=119, w=50, h=50, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
start = M5Btn(text='start', x=130, y=186, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
touch_button0 = M5Btn(text='Button', x=60, y=40, w=200, h=200, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)

from numbers import Number

def h_add_pressed():
  global count, seconds, hours, minutes, vibration_count
  if hours >= 99:
    hours = 0
  else:
    hours = (hours if isinstance(hours, Number) else 0) + 1
  pass
h_add.pressed(h_add_pressed)

def m_add_pressed():
  global count, seconds, hours, minutes, vibration_count
  if minutes >= 59:
    minutes = 0
  else:
    minutes = (minutes if isinstance(minutes, Number) else 0) + 1
  pass
m_add.pressed(m_add_pressed)

def s_add_pressed():
  global count, seconds, hours, minutes, vibration_count
  if seconds >= 59:
    seconds = 0
  else:
    seconds = (seconds if isinstance(seconds, Number) else 0) + 1
  pass
s_add.pressed(s_add_pressed)

def h_reduce_pressed():
  global count, seconds, hours, minutes, vibration_count
  if hours <= 0:
    hours = 99
  else:
    hours = (hours if isinstance(hours, Number) else 0) + -1
  pass
h_reduce.pressed(h_reduce_pressed)

def m_red_pressed():
  global count, seconds, hours, minutes, vibration_count
  if minutes <= 0:
    minutes = 59
  else:
    minutes = (minutes if isinstance(minutes, Number) else 0) + -1
  pass
m_red.pressed(m_red_pressed)

def s_red_pressed():
  global count, seconds, hours, minutes, vibration_count
  if seconds <= 0:
    seconds = 59
  else:
    seconds = (seconds if isinstance(seconds, Number) else 0) + -1
  pass
s_red.pressed(s_red_pressed)

def start_pressed():
  global count, seconds, hours, minutes, vibration_count
  count = (count if isinstance(count, Number) else 0) + 1
  pass
start.pressed(start_pressed)

def touch_button0_pressed():
  global count, seconds, hours, minutes, vibration_count
  touch_button0.set_hidden(True)
  vibration_count = (vibration_count if isinstance(vibration_count, Number) else 0) + 1
  power.setVibrationEnable(False)
  pass
touch_button0.pressed(touch_button0_pressed)


seconds = 0
minutes = 0
hours = 0
count = 0
vibration_count = 1
touch_button0.set_hidden(True)
while True:
  if count % 2 == 1:
    if hours >= 1 and minutes == 0 and seconds == 0:
      minutes = 59
      seconds = 60
      hours = (hours if isinstance(hours, Number) else 0) + -1
    elif hours >= 1 and minutes >= 1 and seconds == 0:
      seconds = 60
      minutes = (minutes if isinstance(minutes, Number) else 0) + -1
    elif hours == 0 and minutes >= 1 and seconds == 0:
      minutes = (minutes if isinstance(minutes, Number) else 0) + -1
      seconds = 60
    elif hours == 0 and minutes == 0 and seconds == 0:
      count = (count if isinstance(count, Number) else 0) + 1
      seconds = (seconds if isinstance(seconds, Number) else 0) + 1
      if vibration_count % 2 == 1:
        power.setVibrationEnable(True)
      vibration_count = (vibration_count if isinstance(vibration_count, Number) else 0) + 1
      touch_button0.set_hidden(False)
    seconds = (seconds if isinstance(seconds, Number) else 0) + -1
    wait(1)
  h.set_text(str(hours))
  m.set_text(str(minutes))
  s.set_text(str(seconds))
  wait_ms(2)
