#note that Core2 at current state only has one frame which means there will be a lot of hide/show take make an illusion as if it has more than 1 frame
from m5stack import * #import m5stack library for Core2 module
from m5stack_ui import * #import m5stack_ui library to be able to send code between UIFlow program and software on Core2  
from uiflow import * #import the UIFlow library
import wifiCfg import wifiCfg #import wifiCfg library to be able to connect to wifi
from m5mqtt import M5mqtt #import M5mqtt, will be used to retrieve weather and events info via mqtt
import time #import library time
from m5stack import touch #import touch library from m5stack, will be used for the slider

screen = M5Screen() #set screen to the screen on module
#clean screen and set it to white color
screen.clean_screen()  
screen.set_screen_bg_color(0xFFFFFF)

#create variables:
previous_brightness_value = None #will contain the previous bightness value
batterysaver_time = None #the time it takes for the screen to go to sleep mode, will be able to be changed in settings
Stopwatch_Start_Stop_Count = None #create variable Stopwatch_Start_Stop_Count and set it to none
Stopwatch_reset_count = None #create variable Stopwatch_reset_count and set it to none
brightness_value = None #current brightness value
batterysaver_previousMillis = None #latest stored ms ticks value
Stopwatch_Hours = None #create variable Stopwatch_Hours and set it to none
Stopwatch_Minutes = None #create variable Stopwatch_Minutes and set it to none
Stopwatch_Seconds = None #create variable Stopwatch_Seconds and set it to none
currentMillis = None #current ms ticks value

wifiCfg.doConnect('SSID', 'PASSWORD') #choose what netowrk to connect to by entering its SSID and password

#create buttons for each smartwatch functions, settings, weather, calendar and stopwatch and set their settings:
Settingsbutton = M5Btn(text='Settings', x=220, y=40, w=80, h=80, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
Weather_button = M5Btn(text='Weather', x=120, y=146, w=80, h=80, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
Calendar_button = M5Btn(text='Calendar', x=120, y=40, w=80, h=80, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
stopwatch_button = M5Btn(text='Stopwatch', x=20, y=40, w=80, h=80, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)

#create label for time and battery status in top bar:
time_topscreen = M5Label('Retrieving time', x=155, y=4, color=0x000, font=FONT_MONT_14, parent=None)
Battery_percentage = M5Label('%', x=83, y=4, color=0x000, font=FONT_MONT_12, parent=None)

#a line is created to seperate and create a top bar section:
line0 = M5Line(x1=0, y1=25, x2=320, y2=25, color=0x000, width=1, parent=None)

from numbers import Number #import Number



def Brightness_level_changed(previous_brightness_value): #create function for slider(Brightness_level_changed)
  #import all variables into function
  global batterysaver_time, Stopwatch_Start_Stop_Count, Stopwatch_reset_count, brightness_value, batterysaver_previousMillis, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds, currentMillis
  screen.set_screen_brightness((Brightness_level.get_value())) #set brightness depending on slider value
  brightness_value = Brightness_level.get_value() #brightness variable gets slider value
  Brightness_level.set_value(brightness_value) #set slider's value depending on the variable bightness' value
  pass
Brightness_level.changed(Brightness_level_changed) #determine when the slider has been changed

def Settingsbutton_pressed(): #function for settings button
  global batterysaver_time, Stopwatch_Start_Stop_Count, Stopwatch_reset_count, brightness_value, previous_brightness_value, batterysaver_previousMillis, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds, currentMillis
  #hide everything in menu except the top bar and show everything in settings section
  Settingsbutton.set_hidden(True)
  Weather_button.set_hidden(True)
  Calendar_button.set_hidden(True)
  stopwatch_button.set_hidden(True)
  Screen_timeout.set_hidden(False)
  Scrren_timeout_seconds.set_hidden(False)
  screen_timeout_decrease.set_hidden(False)
  screen_timeout_increase.set_hidden(False)
  Brightness_level.set_hidden(False)
  Brightness.set_hidden(False)
  #These to lines will appear on all buttons to "reset the timer" for screen sleep or to wake up the screen from sleeping. These two lines will also appear when screen is touched or when the slider is used
  Brightness_level.set_value(brightness_value)
  screen.set_screen_brightness((Brightness_level.get_value()))
  pass
Settingsbutton.pressed(Settingsbutton_pressed) #determine when settings button is pressed

def Calendar_button_pressed(): #function for calendar button
  global batterysaver_time, Stopwatch_Start_Stop_Count, Stopwatch_reset_count, brightness_value, previous_brightness_value, batterysaver_previousMillis, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds, currentMillis
  #hide everything in menu except the top bar and show everything in calendar section
  Settingsbutton.set_hidden(True)
  Weather_button.set_hidden(True)
  Calendar_button.set_hidden(True)
  stopwatch_button.set_hidden(True)
  Calendar_update_event.set_hidden(False)
  Calendar_title.set_hidden(False)
  Calendar_start.set_hidden(False)
  Calendar_end.set_hidden(False)
  Brightness_level.set_value(brightness_value)
  screen.set_screen_brightness((Brightness_level.get_value()))
  pass
Calendar_button.pressed(Calendar_button_pressed) #determine when calendar button is pressed

def start_button_pressed(): #function for start button
  global batterysaver_time, Stopwatch_Start_Stop_Count, Stopwatch_reset_count, brightness_value, previous_brightness_value, batterysaver_previousMillis, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds, currentMillis
  #hide everything in startscreen except the top bar and show everything in menu  
  time_start.set_hidden(True)
  start_button.set_hidden(True)
  Settingsbutton.set_hidden(False)
  Weather_button.set_hidden(False)
  stopwatch_button.set_hidden(False)
  Calendar_button.set_hidden(False)
  Brightness_level.set_value(brightness_value)
  screen.set_screen_brightness((Brightness_level.get_value()))
  pass
start_button.pressed(start_button_pressed) #determine when start button is pressed

def Weather_button_pressed(): #function for weather button
  global batterysaver_time, Stopwatch_Start_Stop_Count, Stopwatch_reset_count, brightness_value, previous_brightness_value, batterysaver_previousMillis, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds, currentMillis
  #hide everything in menu except the top bar and show everything in weather section
  Settingsbutton.set_hidden(True)
  Weather_button.set_hidden(True)
  Calendar_button.set_hidden(True)
  stopwatch_button.set_hidden(True)
  Weather_button_update.set_hidden(False)
  Weather.set_hidden(False)
  Brightness_level.set_value(brightness_value)
  screen.set_screen_brightness((Brightness_level.get_value()))
  pass
Weather_button.pressed(Weather_button_pressed) #determine when weather button is pressed

def stopwatch_button_pressed(): #function for stopwatch button
  global batterysaver_time, Stopwatch_Start_Stop_Count, Stopwatch_reset_count, brightness_value, previous_brightness_value, batterysaver_previousMillis, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds, currentMillis
  #hide everything in menu except the top bar and show everything in stopwatch section
  stopwatch_button.set_hidden(True)
  Settingsbutton.set_hidden(True)
  Weather_button.set_hidden(True)
  Calendar_button.set_hidden(True)
  start_stop_stopwatch_button.set_hidden(False)
  Reset_stopwatch_button.set_hidden(False)
  Hours_.set_hidden(False)
  Minutes_.set_hidden(False)
  Seconds_.set_hidden(False)
  colon1.set_hidden(False)
  colon2.set_hidden(False)
  Brightness_level.set_value(brightness_value)
  screen.set_screen_brightness((Brightness_level.get_value()))
  pass
stopwatch_button.pressed(stopwatch_button_pressed) #determine when stopwatch button is pressed

def Weather_button_update_pressed(): #function for weather update button
  global batterysaver_time, Stopwatch_Start_Stop_Count, Stopwatch_reset_count, brightness_value, previous_brightness_value, batterysaver_previousMillis, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds, currentMillis
  m5mqtt.publish(str('gyarb\\weatherbutton'),str('true')) #update and get weather info through mqtt 
  Brightness_level.set_value(brightness_value)
  screen.set_screen_brightness((Brightness_level.get_value()))
  pass
Weather_button_update.pressed(Weather_button_update_pressed) #determine when weather update button is pressed

def Calendar_update_event_pressed(): #function for calendar update button
  global batterysaver_time, Stopwatch_Start_Stop_Count, Stopwatch_reset_count, brightness_value, previous_brightness_value, batterysaver_previousMillis, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds, currentMillis
  m5mqtt.publish(str('gyarb\\startbutton'),str('true')) #update and get calendar info through mqtt
  Brightness_level.set_value(brightness_value)
  screen.set_screen_brightness((Brightness_level.get_value()))
  pass
Calendar_update_event.pressed(Calendar_update_event_pressed) #determine when calendar update button is pressed

def screen_timeout_increase_pressed(): #function for increasing time (before screen sleep) button
  global batterysaver_time, Stopwatch_Start_Stop_Count, Stopwatch_reset_count, brightness_value, previous_brightness_value, batterysaver_previousMillis, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds, currentMillis
  batterysaver_time = (batterysaver_time if isinstance(batterysaver_time, Number) else 0) + 1000 #when button pressed then add by 1 second to the countdown of the screen sleep
  Brightness_level.set_value(brightness_value)
  screen.set_screen_brightness((Brightness_level.get_value()))
  pass
screen_timeout_increase.pressed(screen_timeout_increase_pressed) #determine when increasing time (before screen sleep) button is pressed

def start_stop_stopwatch_button_pressed(): #function for when start_stop_stopwatch button is pressed
  global batterysaver_time, Stopwatch_Start_Stop_Count, Stopwatch_reset_count, brightness_value, previous_brightness_value, batterysaver_previousMillis, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds, currentMillis
  Stopwatch_Start_Stop_Count = (Stopwatch_Start_Stop_Count if isinstance(Stopwatch_Start_Stop_Count, Number) else 0) + 1 #add 1 to Stopwatch_Start_Stop_Count when pressed
  Brightness_level.set_value(brightness_value)
  screen.set_screen_brightness((Brightness_level.get_value()))
  pass
start_stop_stopwatch_button.pressed(start_stop_stopwatch_button_pressed) #determine when start_stop_stopwatch button is pressed

def screen_timeout_decrease_pressed(): #function for decreasing time (before screen sleep) button
  global batterysaver_time, Stopwatch_Start_Stop_Count, Stopwatch_reset_count, brightness_value, previous_brightness_value, batterysaver_previousMillis, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds, currentMillis
  batterysaver_time = (batterysaver_time if isinstance(batterysaver_time, Number) else 0) + -1000 #when button pressed then reduce by 1 second from the countdown of the screen sleep
  Brightness_level.set_value(brightness_value)
  screen.set_screen_brightness((Brightness_level.get_value()))
  pass
screen_timeout_decrease.pressed(screen_timeout_decrease_pressed) #determine when decreasing time (before screen sleep) button is pressed

def Reset_stopwatch_button_pressed(): #function for when Reset_stopwatch button is pressed
  global batterysaver_time, Stopwatch_Start_Stop_Count, Stopwatch_reset_count, brightness_value, previous_brightness_value, batterysaver_previousMillis, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds, currentMillis
  Stopwatch_reset_count = (Stopwatch_reset_count if isinstance(Stopwatch_reset_count, Number) else 0) + 1 #add 1 to Stopwatch_Start_Stop_Count when pressed
  Brightness_level.set_value(brightness_value)
  screen.set_screen_brightness((Brightness_level.get_value()))
  pass
Reset_stopwatch_button.pressed(Reset_stopwatch_button_pressed) #determine when Reset_stopwatch button is pressed

def fun_gyarb__weather_(topic_data): #function for displaying weather status
  global batterysaver_time, Stopwatch_Start_Stop_Count, Stopwatch_reset_count, brightness_value, previous_brightness_value, batterysaver_previousMillis, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds, currentMillis
  Weather.set_text(str(topic_data)) #display weather info on label "Weather" 
  pass

def fun_gyarb__title_(topic_data): #function for displaying calendar title
  global batterysaver_time, Stopwatch_Start_Stop_Count, Stopwatch_reset_count, brightness_value, previous_brightness_value, batterysaver_previousMillis, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds, currentMillis
  Calendar_title.set_text(str(topic_data)) #display calendar title on label "Calendar_title"
  pass

def fun_gyarb__start_(topic_data): #function for displaying calendar conent
  global batterysaver_time, Stopwatch_Start_Stop_Count, Stopwatch_reset_count, brightness_value, previous_brightness_value, batterysaver_previousMillis, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds, currentMillis
  Calendar_start.set_text(str(topic_data)) #display calendar conent on label "Calendar_start"
  pass

def fun_gyarb__end_(topic_data): #function for displaying last calendar content
  global batterysaver_time, Stopwatch_Start_Stop_Count, Stopwatch_reset_count, brightness_value, previous_brightness_value, batterysaver_previousMillis, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds, currentMillis
  Calendar_end.set_text(str(topic_data)) #display last calendar content on label "Calendar_end"
  pass

def buttonB_wasPressed(): #function for buildt in middle button
  global batterysaver_time, Stopwatch_Start_Stop_Count, Stopwatch_reset_count, brightness_value, previous_brightness_value, batterysaver_previousMillis, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds, currentMillis
  #hide everything except top bar and show everything on start screen
  Brightness.set_hidden(True)
  Brightness_level.set_hidden(True)
  Settingsbutton.set_hidden(True)
  Calendar_button.set_hidden(True)
  Weather_button.set_hidden(True)
  start_button.set_hidden(False)
  start_stop_stopwatch_button.set_hidden(True)
  Reset_stopwatch_button.set_hidden(True)
  stopwatch_button.set_hidden(True)
  time_start.set_hidden(False)
  Hours_.set_hidden(True)
  Minutes_.set_hidden(True)
  Seconds_.set_hidden(True)
  colon1.set_hidden(True)
  colon2.set_hidden(True)
  Calendar_update_event.set_hidden(True)
  Calendar_title.set_hidden(True)
  Calendar_start.set_hidden(True)
  Calendar_end.set_hidden(True)
  Weather_button_update.set_hidden(True)
  Weather.set_hidden(True)
  Screen_timeout.set_hidden(True)
  Scrren_timeout_seconds.set_hidden(True)
  screen_timeout_decrease.set_hidden(True)
  screen_timeout_increase.set_hidden(True)
  Brightness_level.set_value(brightness_value)
  screen.set_screen_brightness((Brightness_level.get_value()))
  pass
btnB.wasPressed(buttonB_wasPressed) #determine when buildt in middle button is pressed


brightness_value = 100 #set variable brightness value to 100
previous_brightness_value = 100 #set previous_brightness value to 100 (max)
batterysaver_previousMillis = 0 #set previousMillis to 0
batterysaver_time = 20000 #set batterysaver_time to 20000ms, 20s before screen sleeps
Brightness_level.set_value(100) #set slider value to 100

#hide everything that is not part of startscreen and top bar:
Settingsbutton.set_hidden(True)
Weather_button.set_hidden(True)
Calendar_button.set_hidden(True)
stopwatch_button.set_hidden(True)
start_stop_stopwatch_button.set_hidden(True)
Reset_stopwatch_button.set_hidden(True)
Brightness_level.set_hidden(True)
Brightness.set_hidden(True)
Hours_.set_hidden(True)
Minutes_.set_hidden(True)
Seconds_.set_hidden(True)
colon1.set_hidden(True)
colon2.set_hidden(True)
Calendar_update_event.set_hidden(True)
Calendar_title.set_hidden(True)
Calendar_start.set_hidden(True)
Calendar_end.set_hidden(True)
Weather_button_update.set_hidden(True)
Weather.set_hidden(True)
Screen_timeout.set_hidden(True)
Scrren_timeout_seconds.set_hidden(True)
screen_timeout_decrease.set_hidden(True)
screen_timeout_increase.set_hidden(True)

#set variables within stopwatch to 0
Stopwatch_Hours = 0
Stopwatch_Minutes = 0
Stopwatch_Seconds = 0
Stopwatch_Start_Stop_Count = 0
Stopwatch_reset_count = 0

m5mqtt = M5mqtt('1', '192.168.1.133', 1883, '', '', 300) #set mqtt configuration
#subscribe to the mqtt topics to retreive info
m5mqtt.subscribe(str('gyarb\\weather'), fun_gyarb__weather_)
m5mqtt.subscribe(str('gyarb\\title'), fun_gyarb__title_)
m5mqtt.subscribe(str('gyarb\\start'), fun_gyarb__start_)
m5mqtt.subscribe(str('gyarb\\end'), fun_gyarb__end_)
m5mqtt.start() #start m5mqtt

while True: #while loop
  #create rectangles and placed them so it creates a battery icon
  lcd.rect(80, 2, 60, 20, color=0x000000)
  lcd.rect(139, 7, 5, 10, color=0x000000)
  #print the RTC time retreived through internet on both time labels
  time_start.set_text(str(rtc.printRTCtime()))
  time_topscreen.set_text(str(rtc.printRTCtime()))
  currentMillis = time.ticks_ms() #set currentmillis to the esp32's ms ticks
  
  if (touch.status()) == 1: #if screen has been touched then:
    batterysaver_previousMillis = currentMillis #set prevmillis to currentmillis
    screen.set_screen_brightness((Brightness_level.get_value()))
    Brightness_level.set_value(brightness_value)
  
  if currentMillis - batterysaver_previousMillis >= batterysaver_time: #if currentmillis - prevmillis is higher or equal to value of batterysaver_time then set prevmillis to currentmillis
    batterysaver_previousMillis = currentMillis
    if (touch.status()) == 0: #if currentmillis - prevmillis is higher or equal to value of batterysaver_time and screen has not been touched within the batterysaver_time period then set brghtness and slider to 10
      screen.set_screen_brightness(10)
      Brightness_level.set_value(10)
  
  if batterysaver_time <= 5000: #variable interval has its lowest value of 5000ms or 5s
    batterysaver_time = 5000
  if batterysaver_time >= 60000: #variable interval has its highest value of 60000ms or 60s
    batterysaver_time = 60000
  Scrren_timeout_seconds.set_text(str(batterysaver_time / 1000)) #divides the value so batterysaver_time (in settings) displays in seconds instead of ms
  
  if Stopwatch_Start_Stop_Count % 2 == 1: #if Stopwatch_Start_Stop_Count is an odd value then:
    if Stopwatch_Seconds >= 59: #if Stopwatch_Start_Stop_Count is an odd value and Stopwatch_Seconds is 59 or higher then:
      Stopwatch_Minutes = (Stopwatch_Minutes if isinstance(Stopwatch_Minutes, Number) else 0) + 1 #add 1 to Stopwatch_Minutes
      Stopwatch_Seconds = -1 #reduce 1 from Stopwatch_Seconds
      if Stopwatch_Minutes >= 59: #if Stopwatch_Start_Stop_Count is an odd value and Stopwatch_Seconds is 59 or higher and Stopwatch_Minutes is 59 or higher then:
        Stopwatch_Hours = (Stopwatch_Hours if isinstance(Stopwatch_Hours, Number) else 0) + 1 #add 1 to Stopwatch_Hours
        Stopwatch_Minutes = 0 #set Stopwatch_Minutes to 0
        if Stopwatch_Hours >= 24: #if Stopwatch_Start_Stop_Count is an odd value and Stopwatch_Seconds is 59 or higher and Stopwatch_Minutes is 59 or higher and Stopwatch_Hours is 24 or higher then set all three values to 0:
          Stopwatch_Seconds = 0 
          Stopwatch_Minutes = 0
          Stopwatch_Hours = 0
    Stopwatch_reset_count = 0 #set Stopwatch_reset_count to 0
    wait_ms(998) #wait 998ms because of the automatic 2ms form while loop
    Stopwatch_Seconds = (Stopwatch_Seconds if isinstance(Stopwatch_Seconds, Number) else 0) + 1 #add 1 to Stopwatch_Seconds
  
  if Stopwatch_reset_count % 2 == 1: #if Stopwatch_reset_count is odd then stop stopwatch and set all three value to 0
    Stopwatch_Start_Stop_Count = 0
    Stopwatch_Seconds = 0
    Stopwatch_Minutes = 0
    Stopwatch_Hours = 0
  Seconds_.set_text(str(Stopwatch_Seconds)) #display Stopwatch_Seconds on label namned "Seconds_"
  Minutes_.set_text(str(Stopwatch_Minutes)) #display Stopwatch_Minutes on label namned "Minutes_"
  Hours_.set_text(str(Stopwatch_Hours)) #display Stopwatch_Hours on label namned "Hours_"
  
  #the position of the variable displaying the battery status will chnage depending on output becasue of the words' width
  if (power.getBatVoltage()) <= 3.65: #if battery voltage is at 3.65V or lower then display “CHARGE”
    Battery_percentage.set_text('CHARGE')
    Battery_percentage.set_pos(83, 4)
  elif (power.getBatVoltage()) <= 3.8: #if battery voltage is at 3.8V or lower then display “LOW”
    Battery_percentage.set_text('LOW')
    Battery_percentage.set_pos(96, 4)
  elif (power.getBatVoltage()) <= 3.95: #if battery voltage is at 3.95V or lower then display “MED”
    Battery_percentage.set_text('MED')
    Battery_percentage.set_pos(96, 4)
  elif (power.getBatVoltage()) <= 4.2: #if battery voltage is at 4.2V or lower then display “HIGH”
    Battery_percentage.set_text('HIGH')
    Battery_percentage.set_pos(94, 4)
  wait_ms(2) #wait 2ms, automatic when using UIFlow and loop
