from m5stack import * #import m5stack library for Core2 module
from m5stack_ui import * #import m5stack_ui library to be able to send code between UIFlow program and software on Core2  
from uiflow import * #import the UIFlow library
import time #import library time
from m5stack import touch #import touch library from m5stack, will be used for the slider

screen = M5Screen() #set screen to the screen on module
#clean screen and set it to white color
screen.clean_screen()  
screen.set_screen_bg_color(0xFFFFFF)

#create variables
prev_brightness = None #will contain the previous bightness value
interval = None #the time it takes for the screen to go to sleep mode, will be able to be changed in settings
brightness = None #current brightness value
prevmillis = None #latest stored millis value
currentmillis = None #current millis value

#create slider for brightness and set settings
slider0 = M5Slider(x=45, y=150, w=200, h=12, min=0, max=100, bg_c=0xa0a0a0, color=0x08A2B0, parent=None)
#create label for the displaying the time before screen sleeps
screensaver_time = M5Label('xx', x=139, y=73, color=0x000, font=FONT_MONT_14, parent=None)
#create buttons for increasing and decreasing the time before screen sleeps
ss_time_dec = M5Btn(text='-', x=44, y=66, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
ss_time_inc = M5Btn(text='+', x=187, y=68, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)

from numbers import Number #import numbers



def slider0_changed(prev_brightness): #create function for slider
  global interval, brightness, prevmillis, currentmillis #import all variables into function
  screen.set_screen_brightness((slider0.get_value())) #set brightness depending on slider value
  brightness = slider0.get_value() #brightness variable gets slider value
  slider0.set_value(brightness) #set slider's value depending on the variable bightness' value
  pass
slider0.changed(slider0_changed) #determine when the slider has been changed

def ss_time_inc_pressed(): #function for increasing time (before screen sleep) button
  global interval, prev_brightness, brightness, prevmillis, currentmillis
  interval = (interval if isinstance(interval, Number) else 0) + 1000 #when button pressed then add by 1 second to the countdown of the screen sleep
  #slider is set to variable brightness value and the screen brightness is set to the slider value. These to lines will appear on all buttons to "reset the timer" for screen sleep and to wake up the screen from sleeping
  slider0.set_value(brightness)
  screen.set_screen_brightness((slider0.get_value()))
  pass
ss_time_inc.pressed(ss_time_inc_pressed) #determine when increasing time (before screen sleep) is pressed

def ss_time_dec_pressed(): #function for decreasing time (before screen sleep) button
  global interval, prev_brightness, brightness, prevmillis, currentmillis
  interval = (interval if isinstance(interval, Number) else 0) + -1000 #when button pressed then reduce by 1 second from the countdown of the screen sleep
  slider0.set_value(brightness)
  screen.set_screen_brightness((slider0.get_value()))
  pass
ss_time_dec.pressed(ss_time_dec_pressed) #determine when decreasing time (before screen sleep) is pressed


prev_brightness = 100 #set prev_brightness to 100 (max)
prevmillis = 0 #set prevmillis to 0
brightness = 100 #set variable brightness value to 100
interval = 5000 #set interval to 5000ms, 5s before screen sleeps
slider0.set_value(100) #set slider value to 100
while True: #while loop
  currentmillis = time.ticks_ms() #set currentmillis to the esp32's ms ticks
  if (touch.status()) == 1: #if the screen is touched then:
    prevmillis = currentmillis #set prevmillis to currentmillis
    screen.set_screen_brightness((slider0.get_value()))
    slider0.set_value(brightness)
  if currentmillis - prevmillis >= interval: #if currentmillis - prevmillis is higher or equal to value of interval then set prevmillis to currentmillis
    prevmillis = currentmillis
    if (touch.status()) == 0: #if currentmillis - prevmillis is higher or equal to value of interval and screen has not been touched within the interval period then set brghtness and slider to 10
      screen.set_screen_brightness(10)
      slider0.set_value(10)
  if interval <= 5000: #variable interval has its lowest value of 5000ms or 5s
    interval = 5000
  if interval >= 60000: #variable interval has its highest value of 60000ms or 60s
    interval = 60000
  screensaver_time.set_text(str(interval)) #display the interval number on screen
  wait_ms(2)
