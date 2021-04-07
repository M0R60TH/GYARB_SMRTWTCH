from m5stack import *
from m5stack_ui import *
from uiflow import *
import wifiCfg
from m5mqtt import M5mqtt
import time
from m5stack import touch

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)


previous_brightness_value = None
batterysaver_time = None
Stopwatch_Start_Stop_Count = None
Stopwatch_reset_count = None
brightness_value = None
batterysaver_previousMillis = None
Stopwatch_Hours = None
Stopwatch_Minutes = None
Stopwatch_Seconds = None
currentMillis = None

wifiCfg.doConnect('', '')
Settingsbutton = M5Btn(text='Settings', x=220, y=40, w=80, h=80, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
Weather_button = M5Btn(text='Weather', x=120, y=146, w=80, h=80, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
Calendar_button = M5Btn(text='Calendar', x=120, y=40, w=80, h=80, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
stopwatch_button = M5Btn(text='Stopwatch', x=20, y=40, w=80, h=80, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
time_topscreen = M5Label('Retrieving time', x=155, y=4, color=0x000, font=FONT_MONT_14, parent=None)
Battery_percentage = M5Label('%', x=83, y=4, color=0x000, font=FONT_MONT_12, parent=None)
line0 = M5Line(x1=0, y1=25, x2=320, y2=25, color=0x000, width=1, parent=None)

from numbers import Number



def Brightness_level_changed(previous_brightness_value):
  global batterysaver_time, Stopwatch_Start_Stop_Count, Stopwatch_reset_count, brightness_value, batterysaver_previousMillis, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds, currentMillis
  screen.set_screen_brightness((Brightness_level.get_value()))
  brightness_value = Brightness_level.get_value()
  Brightness_level.set_value(brightness_value)
  pass
Brightness_level.changed(Brightness_level_changed)

def Settingsbutton_pressed():
  global batterysaver_time, Stopwatch_Start_Stop_Count, Stopwatch_reset_count, brightness_value, previous_brightness_value, batterysaver_previousMillis, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds, currentMillis
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
  Brightness_level.set_value(brightness_value)
  screen.set_screen_brightness((Brightness_level.get_value()))
  pass
Settingsbutton.pressed(Settingsbutton_pressed)

def Calendar_button_pressed():
  global batterysaver_time, Stopwatch_Start_Stop_Count, Stopwatch_reset_count, brightness_value, previous_brightness_value, batterysaver_previousMillis, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds, currentMillis
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
Calendar_button.pressed(Calendar_button_pressed)

def start_button_pressed():
  global batterysaver_time, Stopwatch_Start_Stop_Count, Stopwatch_reset_count, brightness_value, previous_brightness_value, batterysaver_previousMillis, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds, currentMillis
  time_start.set_hidden(True)
  start_button.set_hidden(True)
  Settingsbutton.set_hidden(False)
  Weather_button.set_hidden(False)
  stopwatch_button.set_hidden(False)
  Calendar_button.set_hidden(False)
  Brightness_level.set_value(brightness_value)
  screen.set_screen_brightness((Brightness_level.get_value()))
  pass
start_button.pressed(start_button_pressed)

def Weather_button_pressed():
  global batterysaver_time, Stopwatch_Start_Stop_Count, Stopwatch_reset_count, brightness_value, previous_brightness_value, batterysaver_previousMillis, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds, currentMillis
  Settingsbutton.set_hidden(True)
  Weather_button.set_hidden(True)
  Calendar_button.set_hidden(True)
  stopwatch_button.set_hidden(True)
  Weather_button_update.set_hidden(False)
  Weather.set_hidden(False)
  Brightness_level.set_value(brightness_value)
  screen.set_screen_brightness((Brightness_level.get_value()))
  pass
Weather_button.pressed(Weather_button_pressed)

def stopwatch_button_pressed():
  global batterysaver_time, Stopwatch_Start_Stop_Count, Stopwatch_reset_count, brightness_value, previous_brightness_value, batterysaver_previousMillis, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds, currentMillis
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
stopwatch_button.pressed(stopwatch_button_pressed)

def Weather_button_update_pressed():
  global batterysaver_time, Stopwatch_Start_Stop_Count, Stopwatch_reset_count, brightness_value, previous_brightness_value, batterysaver_previousMillis, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds, currentMillis
  m5mqtt.publish(str('gyarb\\weatherbutton'),str('true'))
  Brightness_level.set_value(brightness_value)
  screen.set_screen_brightness((Brightness_level.get_value()))
  pass
Weather_button_update.pressed(Weather_button_update_pressed)

def Calendar_update_event_pressed():
  global batterysaver_time, Stopwatch_Start_Stop_Count, Stopwatch_reset_count, brightness_value, previous_brightness_value, batterysaver_previousMillis, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds, currentMillis
  m5mqtt.publish(str('gyarb\\startbutton'),str('true'))
  Brightness_level.set_value(brightness_value)
  screen.set_screen_brightness((Brightness_level.get_value()))
  pass
Calendar_update_event.pressed(Calendar_update_event_pressed)

def screen_timeout_increase_pressed():
  global batterysaver_time, Stopwatch_Start_Stop_Count, Stopwatch_reset_count, brightness_value, previous_brightness_value, batterysaver_previousMillis, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds, currentMillis
  batterysaver_time = (batterysaver_time if isinstance(batterysaver_time, Number) else 0) + 1000
  Brightness_level.set_value(brightness_value)
  screen.set_screen_brightness((Brightness_level.get_value()))
  pass
screen_timeout_increase.pressed(screen_timeout_increase_pressed)

def start_stop_stopwatch_button_pressed():
  global batterysaver_time, Stopwatch_Start_Stop_Count, Stopwatch_reset_count, brightness_value, previous_brightness_value, batterysaver_previousMillis, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds, currentMillis
  Stopwatch_Start_Stop_Count = (Stopwatch_Start_Stop_Count if isinstance(Stopwatch_Start_Stop_Count, Number) else 0) + 1
  Brightness_level.set_value(brightness_value)
  screen.set_screen_brightness((Brightness_level.get_value()))
  pass
start_stop_stopwatch_button.pressed(start_stop_stopwatch_button_pressed)

def screen_timeout_decrease_pressed():
  global batterysaver_time, Stopwatch_Start_Stop_Count, Stopwatch_reset_count, brightness_value, previous_brightness_value, batterysaver_previousMillis, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds, currentMillis
  batterysaver_time = (batterysaver_time if isinstance(batterysaver_time, Number) else 0) + -1000
  Brightness_level.set_value(brightness_value)
  screen.set_screen_brightness((Brightness_level.get_value()))
  pass
screen_timeout_decrease.pressed(screen_timeout_decrease_pressed)

def Reset_stopwatch_button_pressed():
  global batterysaver_time, Stopwatch_Start_Stop_Count, Stopwatch_reset_count, brightness_value, previous_brightness_value, batterysaver_previousMillis, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds, currentMillis
  Stopwatch_reset_count = (Stopwatch_reset_count if isinstance(Stopwatch_reset_count, Number) else 0) + 1
  Brightness_level.set_value(brightness_value)
  screen.set_screen_brightness((Brightness_level.get_value()))
  pass
Reset_stopwatch_button.pressed(Reset_stopwatch_button_pressed)

def fun_gyarb__weather_(topic_data):
  global batterysaver_time, Stopwatch_Start_Stop_Count, Stopwatch_reset_count, brightness_value, previous_brightness_value, batterysaver_previousMillis, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds, currentMillis
  Weather.set_text(str(topic_data))
  pass

def fun_gyarb__title_(topic_data):
  global batterysaver_time, Stopwatch_Start_Stop_Count, Stopwatch_reset_count, brightness_value, previous_brightness_value, batterysaver_previousMillis, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds, currentMillis
  Calendar_title.set_text(str(topic_data))
  pass

def fun_gyarb__start_(topic_data):
  global batterysaver_time, Stopwatch_Start_Stop_Count, Stopwatch_reset_count, brightness_value, previous_brightness_value, batterysaver_previousMillis, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds, currentMillis
  Calendar_start.set_text(str(topic_data))
  pass

def fun_gyarb__end_(topic_data):
  global batterysaver_time, Stopwatch_Start_Stop_Count, Stopwatch_reset_count, brightness_value, previous_brightness_value, batterysaver_previousMillis, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds, currentMillis
  Calendar_end.set_text(str(topic_data))
  pass

def buttonB_wasPressed():
  global batterysaver_time, Stopwatch_Start_Stop_Count, Stopwatch_reset_count, brightness_value, previous_brightness_value, batterysaver_previousMillis, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds, currentMillis
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
btnB.wasPressed(buttonB_wasPressed)


brightness_value = 100
previous_brightness_value = 100
batterysaver_previousMillis = 0
batterysaver_time = 20000
Brightness_level.set_value(100)
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
Stopwatch_Hours = 0
Stopwatch_Minutes = 0
Stopwatch_Seconds = 0
Stopwatch_Start_Stop_Count = 0
Stopwatch_reset_count = 0
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
m5mqtt = M5mqtt('1', '192.168.1.133', 1883, '', '', 300)
m5mqtt.subscribe(str('gyarb\\weather'), fun_gyarb__weather_)
m5mqtt.subscribe(str('gyarb\\title'), fun_gyarb__title_)
m5mqtt.subscribe(str('gyarb\\start'), fun_gyarb__start_)
m5mqtt.subscribe(str('gyarb\\end'), fun_gyarb__end_)
m5mqtt.start()
while True:
  lcd.rect(80, 2, 60, 20, color=0x000000)
  lcd.rect(139, 7, 5, 10, color=0x000000)
  time_start.set_text(str(rtc.printRTCtime()))
  time_topscreen.set_text(str(rtc.printRTCtime()))
  currentMillis = time.ticks_ms()
  if (touch.status()) == 1:
    batterysaver_previousMillis = currentMillis
    screen.set_screen_brightness((Brightness_level.get_value()))
    Brightness_level.set_value(brightness_value)
  if currentMillis - batterysaver_previousMillis >= batterysaver_time:
    batterysaver_previousMillis = currentMillis
    if (touch.status()) == 0:
      screen.set_screen_brightness(10)
      Brightness_level.set_value(10)
  if batterysaver_time <= 5000:
    batterysaver_time = 5000
  if batterysaver_time >= 60000:
    batterysaver_time = 60000
  Scrren_timeout_seconds.set_text(str(batterysaver_time / 1000))
  if Stopwatch_Start_Stop_Count % 2 == 1:
    if Stopwatch_Seconds >= 59:
      Stopwatch_Minutes = (Stopwatch_Minutes if isinstance(Stopwatch_Minutes, Number) else 0) + 1
      Stopwatch_Seconds = -1
      if Stopwatch_Minutes >= 59:
        Stopwatch_Hours = (Stopwatch_Hours if isinstance(Stopwatch_Hours, Number) else 0) + 1
        Stopwatch_Minutes = 0
        if Stopwatch_Hours >= 24:
          Stopwatch_Seconds = 0
          Stopwatch_Minutes = 0
          Stopwatch_Hours = 0
    Stopwatch_reset_count = 0
    wait_ms(998)
    Stopwatch_Seconds = (Stopwatch_Seconds if isinstance(Stopwatch_Seconds, Number) else 0) + 1
  if Stopwatch_reset_count % 2 == 1:
    Stopwatch_Start_Stop_Count = 0
    Stopwatch_Seconds = 0
    Stopwatch_Minutes = 0
    Stopwatch_Hours = 0
  Seconds_.set_text(str(Stopwatch_Seconds))
  Minutes_.set_text(str(Stopwatch_Minutes))
  Hours_.set_text(str(Stopwatch_Hours))
  if (power.getBatVoltage()) <= 3.65:
    Battery_percentage.set_text('CHARGE')
    Battery_percentage.set_pos(83, 4)
  elif (power.getBatVoltage()) <= 3.8:
    Battery_percentage.set_text('LOW')
    Battery_percentage.set_pos(96, 4)
  elif (power.getBatVoltage()) <= 3.95:
    Battery_percentage.set_text('MED')
    Battery_percentage.set_pos(96, 4)
  elif (power.getBatVoltage()) <= 4.2:
    Battery_percentage.set_text('HIGH')
    Battery_percentage.set_pos(94, 4)
  wait_ms(2)
