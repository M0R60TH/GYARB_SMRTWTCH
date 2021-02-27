from m5stack import *
from m5stack_ui import *
from uiflow import *
import wifiCfg
import time

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)


brightness_value = None
Stopwatch_Start_Stop_Count = None
Stopwatch_reset_count = None
Timer_Start_Pause_button_count = None
Timer_Hours = None
Timer_Minutes = None
Timer_Seconds = None
Timer_vibration_count = None
Stopwatch_Hours = None
Stopwatch_Minutes = None
Stopwatch_Seconds = None

wifiCfg.doConnect('SSID', 'PASSWORD')
time_start = M5Label('Retrieving time', x=5, y=47, color=0x000, font=FONT_MONT_26, parent=None)
start_button = M5Btn(text='Press to continue', x=35, y=140, w=250, h=70, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
line6 = M5Line(x1=160, y1=0, x2=160, y2=240, color=0xff0000, width=1, parent=None)
Settingsbutton = M5Btn(text='Settings', x=220, y=40, w=80, h=80, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
Pulse_button = M5Btn(text='Pulse', x=220, y=146, w=80, h=80, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
Weather_button = M5Btn(text='Weather', x=120, y=146, w=80, h=80, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
Time_button = M5Btn(text='Time', x=20, y=40, w=80, h=80, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
Calendar_button = M5Btn(text='Calendar', x=120, y=40, w=80, h=80, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
Music_button = M5Btn(text='Music', x=20, y=146, w=80, h=80, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
Hours_ = M5Label('00', x=48, y=45, color=0x000, font=FONT_MONT_48, parent=None)
Minutes_ = M5Label('00', x=128, y=45, color=0x000, font=FONT_MONT_48, parent=None)
Seconds_ = M5Label('00', x=208, y=45, color=0x000, font=FONT_MONT_48, parent=None)
colon2 = M5Label(':', x=193, y=42, color=0x000, font=FONT_MONT_48, parent=None)
colon1 = M5Label(':', x=114, y=42, color=0x000, font=FONT_MONT_48, parent=None)
colon3 = M5Label(':', x=114, y=67, color=0x000, font=FONT_MONT_48, parent=None)
colon4 = M5Label(':', x=193, y=67, color=0x000, font=FONT_MONT_48, parent=None)
Brightness_level = M5Slider(x=10, y=70, w=270, h=15, min=0, max=100, bg_c=0xa0a0a0, color=0x08A2B0, parent=None)
Brightness = M5Label('Brightness Level', x=10, y=40, color=0x000, font=FONT_MONT_20, parent=None)
line1 = M5Line(x1=0, y1=132, x2=320, y2=132, color=0x000, width=1, parent=None)
timer_button = M5Btn(text='Timer', x=30, y=85, w=100, h=100, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
stopwatch_button = M5Btn(text='Stopwatch', x=190, y=85, w=100, h=100, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
start_stop_stopwatch_button = M5Btn(text='Start / Stop', x=110, y=100, w=100, h=60, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
Timer_seconds_ = M5Label('00', x=208, y=70, color=0x000, font=FONT_MONT_48, parent=None)
Timer_minutes_ = M5Label('00', x=128, y=70, color=0x000, font=FONT_MONT_48, parent=None)
Timer_hours_ = M5Label('00', x=48, y=70, color=0x000, font=FONT_MONT_48, parent=None)
Reset_stopwatch_button = M5Btn(text='Reset', x=110, y=170, w=100, h=60, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
Timer_start_pause = M5Btn(text='Start / Pause', x=95, y=170, w=130, h=60, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
Timer_Hours_Increase = M5Btn(text='+', x=52, y=38, w=40, h=40, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_48, parent=None)
Timer_Hours_Decrease = M5Btn(text='-', x=52, y=114, w=40, h=40, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_48, parent=None)
line5 = M5Line(x1=0, y1=120, x2=320, y2=120, color=0xff0000, width=1, parent=None)
time_topscreen = M5Label('Retrieving time', x=155, y=4, color=0x000, font=FONT_MONT_14, parent=None)
Battery_percentage = M5Label('%', x=83, y=4, color=0x000, font=FONT_MONT_12, parent=None)
Timer_Minutes_Decrease = M5Btn(text='-', x=132, y=114, w=40, h=40, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_48, parent=None)
Timer_Seconds_Decrease = M5Btn(text='-', x=210, y=114, w=40, h=40, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_48, parent=None)
Timer_Minutes_Increase = M5Btn(text='+', x=132, y=38, w=40, h=40, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_48, parent=None)
Timer_Seconds_Increase = M5Btn(text='+', x=210, y=38, w=40, h=40, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_48, parent=None)
line0 = M5Line(x1=0, y1=25, x2=320, y2=25, color=0x000, width=1, parent=None)
Back_button_stopwatch_timer = M5Btn(text='Back', x=0, y=200, w=90, h=40, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
Timer_Dismiss_button = M5Btn(text='Dismiss', x=0, y=25, w=320, h=215, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_48, parent=None)

from numbers import Number



def Brightness_level_changed(brightness_value):
  global Stopwatch_Start_Stop_Count, Stopwatch_reset_count, Timer_Start_Pause_button_count, Timer_Hours, Timer_Minutes, Timer_Seconds, Timer_vibration_count, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds
  screen.set_screen_brightness(brightness_value)
  pass
Brightness_level.changed(Brightness_level_changed)

def start_button_pressed():
  global Stopwatch_Start_Stop_Count, Stopwatch_reset_count, Timer_Start_Pause_button_count, brightness_value, Timer_Hours, Timer_Minutes, Timer_Seconds, Timer_vibration_count, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds
  time_start.set_hidden(True)
  start_button.set_hidden(True)
  Settingsbutton.set_hidden(False)
  Pulse_button.set_hidden(False)
  Weather_button.set_hidden(False)
  Time_button.set_hidden(False)
  Calendar_button.set_hidden(False)
  Music_button.set_hidden(False)
  pass
start_button.pressed(start_button_pressed)

def Settingsbutton_pressed():
  global Stopwatch_Start_Stop_Count, Stopwatch_reset_count, Timer_Start_Pause_button_count, brightness_value, Timer_Hours, Timer_Minutes, Timer_Seconds, Timer_vibration_count, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds
  Settingsbutton.set_hidden(True)
  Pulse_button.set_hidden(True)
  Weather_button.set_hidden(True)
  Time_button.set_hidden(True)
  Calendar_button.set_hidden(True)
  Music_button.set_hidden(True)
  Brightness_level.set_hidden(False)
  Brightness.set_hidden(False)
  pass
Settingsbutton.pressed(Settingsbutton_pressed)

def Time_button_pressed():
  global Stopwatch_Start_Stop_Count, Stopwatch_reset_count, Timer_Start_Pause_button_count, brightness_value, Timer_Hours, Timer_Minutes, Timer_Seconds, Timer_vibration_count, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds
  Settingsbutton.set_hidden(True)
  Pulse_button.set_hidden(True)
  Weather_button.set_hidden(True)
  Time_button.set_hidden(True)
  Calendar_button.set_hidden(True)
  Music_button.set_hidden(True)
  timer_button.set_hidden(False)
  stopwatch_button.set_hidden(False)
  pass
Time_button.pressed(Time_button_pressed)

def stopwatch_button_pressed():
  global Stopwatch_Start_Stop_Count, Stopwatch_reset_count, Timer_Start_Pause_button_count, brightness_value, Timer_Hours, Timer_Minutes, Timer_Seconds, Timer_vibration_count, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds
  timer_button.set_hidden(True)
  stopwatch_button.set_hidden(True)
  start_stop_stopwatch_button.set_hidden(False)
  Reset_stopwatch_button.set_hidden(False)
  Back_button_stopwatch_timer.set_hidden(False)
  Hours_.set_hidden(False)
  Minutes_.set_hidden(False)
  Seconds_.set_hidden(False)
  colon1.set_hidden(False)
  colon2.set_hidden(False)
  pass
stopwatch_button.pressed(stopwatch_button_pressed)

def timer_button_pressed():
  global Stopwatch_Start_Stop_Count, Stopwatch_reset_count, Timer_Start_Pause_button_count, brightness_value, Timer_Hours, Timer_Minutes, Timer_Seconds, Timer_vibration_count, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds
  timer_button.set_hidden(True)
  stopwatch_button.set_hidden(True)
  Timer_start_pause.set_hidden(False)
  Timer_Hours_Increase.set_hidden(False)
  Timer_Hours_Decrease.set_hidden(False)
  Timer_Minutes_Increase.set_hidden(False)
  Timer_Minutes_Decrease.set_hidden(False)
  Timer_Seconds_Increase.set_hidden(False)
  Timer_Seconds_Decrease.set_hidden(False)
  Back_button_stopwatch_timer.set_hidden(False)
  Timer_seconds_.set_hidden(False)
  Timer_minutes_.set_hidden(False)
  Timer_hours_.set_hidden(False)
  colon3.set_hidden(False)
  colon4.set_hidden(False)
  pass
timer_button.pressed(timer_button_pressed)

def start_stop_stopwatch_button_pressed():
  global Stopwatch_Start_Stop_Count, Stopwatch_reset_count, Timer_Start_Pause_button_count, brightness_value, Timer_Hours, Timer_Minutes, Timer_Seconds, Timer_vibration_count, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds
  Stopwatch_Start_Stop_Count = (Stopwatch_Start_Stop_Count if isinstance(Stopwatch_Start_Stop_Count, Number) else 0) + 1
  pass
start_stop_stopwatch_button.pressed(start_stop_stopwatch_button_pressed)

def Reset_stopwatch_button_pressed():
  global Stopwatch_Start_Stop_Count, Stopwatch_reset_count, Timer_Start_Pause_button_count, brightness_value, Timer_Hours, Timer_Minutes, Timer_Seconds, Timer_vibration_count, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds
  Stopwatch_reset_count = (Stopwatch_reset_count if isinstance(Stopwatch_reset_count, Number) else 0) + 1
  pass
Reset_stopwatch_button.pressed(Reset_stopwatch_button_pressed)

def Timer_Hours_Increase_pressed():
  global Stopwatch_Start_Stop_Count, Stopwatch_reset_count, Timer_Start_Pause_button_count, brightness_value, Timer_Hours, Timer_Minutes, Timer_Seconds, Timer_vibration_count, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds
  if Timer_Hours >= 99:
    Timer_Hours = 0
  else:
    Timer_Hours = (Timer_Hours if isinstance(Timer_Hours, Number) else 0) + 1
  pass
Timer_Hours_Increase.pressed(Timer_Hours_Increase_pressed)

def Timer_Hours_Decrease_pressed():
  global Stopwatch_Start_Stop_Count, Stopwatch_reset_count, Timer_Start_Pause_button_count, brightness_value, Timer_Hours, Timer_Minutes, Timer_Seconds, Timer_vibration_count, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds
  if Timer_Hours <= 0:
    Timer_Hours = 99
  else:
    Timer_Hours = (Timer_Hours if isinstance(Timer_Hours, Number) else 0) + -1
  pass
Timer_Hours_Decrease.pressed(Timer_Hours_Decrease_pressed)

def Timer_Minutes_Increase_pressed():
  global Stopwatch_Start_Stop_Count, Stopwatch_reset_count, Timer_Start_Pause_button_count, brightness_value, Timer_Hours, Timer_Minutes, Timer_Seconds, Timer_vibration_count, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds
  if Timer_Minutes >= 59:
    Timer_Minutes = 0
  else:
    Timer_Minutes = (Timer_Minutes if isinstance(Timer_Minutes, Number) else 0) + 1
  pass
Timer_Minutes_Increase.pressed(Timer_Minutes_Increase_pressed)

def Timer_Minutes_Decrease_pressed():
  global Stopwatch_Start_Stop_Count, Stopwatch_reset_count, Timer_Start_Pause_button_count, brightness_value, Timer_Hours, Timer_Minutes, Timer_Seconds, Timer_vibration_count, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds
  if Timer_Hours <= 0:
    Timer_Minutes = 59
  else:
    Timer_Minutes = (Timer_Minutes if isinstance(Timer_Minutes, Number) else 0) + -1
  pass
Timer_Minutes_Decrease.pressed(Timer_Minutes_Decrease_pressed)

def Timer_Seconds_Increase_pressed():
  global Stopwatch_Start_Stop_Count, Stopwatch_reset_count, Timer_Start_Pause_button_count, brightness_value, Timer_Hours, Timer_Minutes, Timer_Seconds, Timer_vibration_count, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds
  if Timer_Seconds >= 59:
    Timer_Seconds = 0
  else:
    Timer_Seconds = (Timer_Seconds if isinstance(Timer_Seconds, Number) else 0) + 1
  pass
Timer_Seconds_Increase.pressed(Timer_Seconds_Increase_pressed)

def Timer_Seconds_Decrease_pressed():
  global Stopwatch_Start_Stop_Count, Stopwatch_reset_count, Timer_Start_Pause_button_count, brightness_value, Timer_Hours, Timer_Minutes, Timer_Seconds, Timer_vibration_count, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds
  if Timer_Seconds <= 0:
    Timer_Seconds = 59
  else:
    Timer_Seconds = (Timer_Seconds if isinstance(Timer_Seconds, Number) else 0) + -1
  pass
Timer_Seconds_Decrease.pressed(Timer_Seconds_Decrease_pressed)

def Timer_start_pause_pressed():
  global Stopwatch_Start_Stop_Count, Stopwatch_reset_count, Timer_Start_Pause_button_count, brightness_value, Timer_Hours, Timer_Minutes, Timer_Seconds, Timer_vibration_count, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds
  Timer_Start_Pause_button_count = (Timer_Start_Pause_button_count if isinstance(Timer_Start_Pause_button_count, Number) else 0) + 1
  pass
Timer_start_pause.pressed(Timer_start_pause_pressed)

def Timer_Dismiss_button_pressed():
  global Stopwatch_Start_Stop_Count, Stopwatch_reset_count, Timer_Start_Pause_button_count, brightness_value, Timer_Hours, Timer_Minutes, Timer_Seconds, Timer_vibration_count, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds
  power.setVibrationEnable(False)
  Timer_Dismiss_button.set_hidden(True)
  Timer_vibration_count = (Timer_vibration_count if isinstance(Timer_vibration_count, Number) else 0) + 1
  pass
Timer_Dismiss_button.pressed(Timer_Dismiss_button_pressed)

def Back_button_stopwatch_timer_pressed():
  global Stopwatch_Start_Stop_Count, Stopwatch_reset_count, Timer_Start_Pause_button_count, brightness_value, Timer_Hours, Timer_Minutes, Timer_Seconds, Timer_vibration_count, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds
  Hours_.set_hidden(True)
  Minutes_.set_hidden(True)
  Seconds_.set_hidden(True)
  colon2.set_hidden(True)
  colon1.set_hidden(True)
  Timer_hours_.set_hidden(True)
  Timer_minutes_.set_hidden(True)
  Timer_seconds_.set_hidden(True)
  colon3.set_hidden(True)
  colon4.set_hidden(True)
  start_stop_stopwatch_button.set_hidden(True)
  Reset_stopwatch_button.set_hidden(True)
  timer_button.set_hidden(False)
  stopwatch_button.set_hidden(False)
  Timer_Hours_Increase.set_hidden(True)
  Timer_Hours_Decrease.set_hidden(True)
  Timer_Minutes_Increase.set_hidden(True)
  Timer_Minutes_Decrease.set_hidden(True)
  Timer_Seconds_Increase.set_hidden(True)
  Timer_Seconds_Decrease.set_hidden(True)
  Timer_start_pause.set_hidden(True)
  Back_button_stopwatch_timer.set_hidden(True)
  pass
Back_button_stopwatch_timer.pressed(Back_button_stopwatch_timer_pressed)

def buttonB_wasPressed():
  global Stopwatch_Start_Stop_Count, Stopwatch_reset_count, Timer_Start_Pause_button_count, brightness_value, Timer_Hours, Timer_Minutes, Timer_Seconds, Timer_vibration_count, Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds
  Brightness.set_hidden(True)
  Brightness_level.set_hidden(True)
  Settingsbutton.set_hidden(True)
  Settingsbutton.set_hidden(True)
  Pulse_button.set_hidden(True)
  Music_button.set_hidden(True)
  Calendar_button.set_hidden(True)
  Weather_button.set_hidden(True)
  Time_button.set_hidden(True)
  start_button.set_hidden(False)
  start_stop_stopwatch_button.set_hidden(True)
  Reset_stopwatch_button.set_hidden(True)
  Back_button_stopwatch_timer.set_hidden(True)
  timer_button.set_hidden(True)
  stopwatch_button.set_hidden(True)
  time_start.set_hidden(False)
  Hours_.set_hidden(True)
  Minutes_.set_hidden(True)
  Seconds_.set_hidden(True)
  colon1.set_hidden(True)
  colon2.set_hidden(True)
  Timer_seconds_.set_hidden(True)
  Timer_minutes_.set_hidden(True)
  Timer_hours_.set_hidden(True)
  colon3.set_hidden(True)
  colon4.set_hidden(True)
  Timer_Hours_Increase.set_hidden(True)
  Timer_Hours_Decrease.set_hidden(True)
  Timer_Minutes_Increase.set_hidden(True)
  Timer_Minutes_Decrease.set_hidden(True)
  Timer_Seconds_Increase.set_hidden(True)
  Timer_Seconds_Decrease.set_hidden(True)
  Timer_start_pause.set_hidden(True)
  pass
btnB.wasPressed(buttonB_wasPressed)


brightness_value = 50
Settingsbutton.set_hidden(True)
Pulse_button.set_hidden(True)
Weather_button.set_hidden(True)
Time_button.set_hidden(True)
Calendar_button.set_hidden(True)
Music_button.set_hidden(True)
timer_button.set_hidden(True)
stopwatch_button.set_hidden(True)
start_stop_stopwatch_button.set_hidden(True)
Reset_stopwatch_button.set_hidden(True)
Back_button_stopwatch_timer.set_hidden(True)
Timer_start_pause.set_hidden(True)
Timer_Dismiss_button.set_hidden(True)
Timer_Hours_Increase.set_hidden(True)
Timer_Hours_Decrease.set_hidden(True)
Timer_Minutes_Increase.set_hidden(True)
Timer_Minutes_Decrease.set_hidden(True)
Timer_Seconds_Increase.set_hidden(True)
Timer_Seconds_Decrease.set_hidden(True)
Brightness_level.set_hidden(True)
Brightness.set_hidden(True)
Hours_.set_hidden(True)
Minutes_.set_hidden(True)
Seconds_.set_hidden(True)
colon1.set_hidden(True)
colon2.set_hidden(True)
Timer_seconds_.set_hidden(True)
Timer_minutes_.set_hidden(True)
Timer_hours_.set_hidden(True)
colon3.set_hidden(True)
colon4.set_hidden(True)
Stopwatch_Hours = 0
Stopwatch_Minutes = 0
Stopwatch_Seconds = 0
Stopwatch_Start_Stop_Count = 0
Stopwatch_reset_count = 0
Timer_Hours = 0
Timer_Minutes = 0
Timer_Seconds = 0
Timer_vibration_count = 0
Timer_Start_Pause_button_count = 0
lcd.rect(80, 2, 60, 20, color=0x000000)
lcd.rect(139, 7, 5, 10, color=0x000000)
while True:
  time_start.set_text(str(rtc.printRTCtime()))
  time_topscreen.set_text(str(rtc.printRTCtime()))
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
    wait(1)
    Stopwatch_Seconds = (Stopwatch_Seconds if isinstance(Stopwatch_Seconds, Number) else 0) + 1
  if Stopwatch_reset_count % 2 == 1:
    Stopwatch_Start_Stop_Count = 0
    Stopwatch_Seconds = 0
    Stopwatch_Minutes = 0
    Stopwatch_Hours = 0
  Seconds_.set_text(str(Stopwatch_Seconds))
  Minutes_.set_text(str(Stopwatch_Minutes))
  Hours_.set_text(str(Stopwatch_Hours))
  if Timer_Start_Pause_button_count % 2 == 1:
    if Timer_Hours >= 1 and Timer_Minutes == 0 and Timer_Seconds == 0:
      Timer_Minutes = 59
      Timer_Seconds = 60
      Timer_Hours = (Timer_Hours if isinstance(Timer_Hours, Number) else 0) + -1
    elif Timer_Hours >= 1 and Timer_Minutes >= 1 and Timer_Seconds == 0:
      Timer_Seconds = 60
      Timer_Minutes = (Timer_Minutes if isinstance(Timer_Minutes, Number) else 0) + -1
    elif Timer_Hours == 0 and Timer_Minutes >= 1 and Timer_Seconds == 0:
      Timer_Seconds = 60
      Timer_Minutes = (Timer_Minutes if isinstance(Timer_Minutes, Number) else 0) + -1
    elif Timer_Hours == 0 and Timer_Minutes == 0 and Timer_Seconds == 0:
      Timer_Seconds = (Timer_Seconds if isinstance(Timer_Seconds, Number) else 0) + 1
      Timer_Start_Pause_button_count = (Timer_Start_Pause_button_count if isinstance(Timer_Start_Pause_button_count, Number) else 0) + 1
      if Timer_vibration_count % 2 == 0:
        power.setVibrationEnable(True)
      Timer_vibration_count = (Timer_vibration_count if isinstance(Timer_vibration_count, Number) else 0) + 1
      Timer_Dismiss_button.set_hidden(False)
    Timer_Seconds = (Timer_Seconds if isinstance(Timer_Seconds, Number) else 0) + -1
    wait(1)
  Timer_hours_.set_text(str(Timer_Hours))
  Timer_minutes_.set_text(str(Timer_Minutes))
  Timer_seconds_.set_text(str(Timer_Seconds))
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
