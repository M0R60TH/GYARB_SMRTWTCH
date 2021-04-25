from m5stack import * #import m5stack library for Core2 module
from m5stack_ui import * #import m5stack_ui library to be able to send code between UIFlow program and software on Core2  
from uiflow import * #import the UIFlow library
import time #import library time

screen = M5Screen() #set screen to the screen on module
#clean screen and set it to white color
screen.clean_screen()  
screen.set_screen_bg_color(0xFFFFFF)

#create variable
count = None #will be used to count the button pressing
seconds = None #variable for the seconds
hours = None #variable for hours
minutes = None #variable for minutes
vibration_count = None #will be used to determine when to vibrate

#create  label for seconds, minutes and hours and set their settings
h = M5Label('00', x=63, y=67, color=0x000, font=FONT_MONT_48, parent=None)
m = M5Label('00', x=128, y=67, color=0x000, font=FONT_MONT_48, parent=None)
s = M5Label('00', x=197, y=67, color=0x000, font=FONT_MONT_48, parent=None)
#add buttons for reducing seconds, minutes, hours, buttons for increasing seconds, minutes, hours, button for start and dismiss. Set their settings
h_add = M5Btn(text='+', x=59, y=10, w=50, h=50, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
h_reduce = M5Btn(text='-', x=63, y=111, w=50, h=50, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
m_add = M5Btn(text='+', x=124, y=10, w=50, h=50, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
s_add = M5Btn(text='+', x=197, y=10, w=50, h=50, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
m_red = M5Btn(text='-', x=136, y=119, w=50, h=50, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
s_red = M5Btn(text='-', x=213, y=119, w=50, h=50, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
start = M5Btn(text='start', x=130, y=186, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
touch_button0 = M5Btn(text='Button', x=60, y=40, w=200, h=200, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None) #dismiss button

from numbers import Number #import library for numbers
 
def h_add_pressed(): #function for increasing value of hours
  global count, seconds, hours, minutes, vibration_count #import all variable into function
  if hours >= 99: #if adding on more than 99 hrs then set it to 0 hours instead of 100 hrs
    hours = 0
  else: #else increase hours by 1 as normal
    hours = (hours if isinstance(hours, Number) else 0) + 1
  pass
h_add.pressed(h_add_pressed) #determine when increase hrs button is pressed

def m_add_pressed(): #function for increasing value of minutes
  global count, seconds, hours, minutes, vibration_count
  if minutes >= 59: #if adding on more than 59 min then set it to 0 min instead of 60 min
    minutes = 0
  else: #else increase minutes by 1 as normal
    minutes = (minutes if isinstance(minutes, Number) else 0) + 1
  pass
m_add.pressed(m_add_pressed) #determine when increase min button is pressed

def s_add_pressed(): #function for increasing value of seconds
  global count, seconds, hours, minutes, vibration_count
  if seconds >= 59: #if adding on more than 59 sec then set it to 0 sec instead of 60 sec
    seconds = 0
  else: #else increase seconds by 1 as normal
    seconds = (seconds if isinstance(seconds, Number) else 0) + 1
  pass
s_add.pressed(s_add_pressed) #determine when increase sec button is pressed

def h_reduce_pressed(): #function for decreasing value of hours
  global count, seconds, hours, minutes, vibration_count
  if hours <= 0: #if reducing more than 0 hours then set it to 99 hours instead of -1 hours
    hours = 99
  else: #else decrease hours by 1 as normal
    hours = (hours if isinstance(hours, Number) else 0) + -1
  pass
h_reduce.pressed(h_reduce_pressed) #determine when decrease hrs button is pressed

def m_red_pressed(): #function for decreasing value of minutes
  global count, seconds, hours, minutes, vibration_count
  if minutes <= 0: #if reducing more than 0 minutes then set it to 59 minutes instead of -1 minutes
    minutes = 59
  else: #else decrease minutes by 1 as normal
    minutes = (minutes if isinstance(minutes, Number) else 0) + -1
  pass
m_red.pressed(m_red_pressed) #determine when decrease min button is pressed

def s_red_pressed(): #function for decreasing value of seconds
  global count, seconds, hours, minutes, vibration_count
  if seconds <= 0: #if reducing more than 0 seconds then set it to 59 seconds instead of -1 seconds
    seconds = 59
  else: #else decrease seconds by 1 as normal
    seconds = (seconds if isinstance(seconds, Number) else 0) + -1
  pass
s_red.pressed(s_red_pressed) #determine when decrease sec button is pressed

def start_pressed(): #function for start button
  global count, seconds, hours, minutes, vibration_count
  count = (count if isinstance(count, Number) else 0) + 1 #increase variable count when start buttons is pressed
  pass
start.pressed(start_pressed) #determine when start button is pressed

def touch_button0_pressed(): #function for dismissing the vibration alarm
  global count, seconds, hours, minutes, vibration_count
  touch_button0.set_hidden(True) #hide the button
  vibration_count = (vibration_count if isinstance(vibration_count, Number) else 0) + 1 #add 1 to the vibration_count is pressed to turn off the vibration caused when timer runs out 
  power.setVibrationEnable(False)
  pass
touch_button0.pressed(touch_button0_pressed) #determine when dismiss button is pressed

#set variables to 0
seconds = 0 #will be used to display the second figure
minutes = 0 #will be used to display the minute figure
hours = 0 #will be used to display the hour figure
count = 0 #will count the pressing of start button
vibration_count = 1 #set vibration_count to 1, ready to vibrate when timer is activated and runs out, dismiss buttons will disable the vibrator
touch_button0.set_hidden(True)  #hide dismiss button
while True: #while loop
  if count % 2 == 1: #if count variable is odd then start timer
    if hours >= 1 and minutes == 0 and seconds == 0: #if timer reaches x:00:00 where x is 1 or higher then:
      minutes = 59 #set minutes to 59
      seconds = 60 #set seconds to 60
      hours = (hours if isinstance(hours, Number) else 0) + -1 #reduce hours by 1
    elif hours >= 1 and minutes >= 1 and seconds == 0: #if timer reaches x:m:00 where x and m is 1 or higher then:
      seconds = 60 #set seconds to 60
      minutes = (minutes if isinstance(minutes, Number) else 0) + -1 #recude minutes by 1
    elif hours == 0 and minutes >= 1 and seconds == 0: #if timer reaches 00:m:00 where m is 1 or higher then:
      minutes = (minutes if isinstance(minutes, Number) else 0) + -1 #reduce minutes by 1
      seconds = 60 #set seconds to 60
    elif hours == 0 and minutes == 0 and seconds == 0: #if timer reaches 00:00:00 then:
      count = (count if isinstance(count, Number) else 0) + 1 #change variable count by 1
      seconds = (seconds if isinstance(seconds, Number) else 0) + 1 #increase seconds by 1
      if vibration_count % 2 == 1: #if vibration_count is odd and timer is at 00:00:00 (after timer was running) then turn on vibration
        power.setVibrationEnable(True) 
      vibration_count = (vibration_count if isinstance(vibration_count, Number) else 0) + 1 #chnage vibration_count by 1
      touch_button0.set_hidden(False) #show dismiss button
    seconds = (seconds if isinstance(seconds, Number) else 0) + -1 #reduce seconds by 1
    wait(1) #wait 1 second
  h.set_text(str(hours)) #display hours figure on label namned hours
  m.set_text(str(minutes)) #display minutes figure on label namned minutes
  s.set_text(str(seconds)) #display seconds figure on label namned seconds
  wait_ms(2)
