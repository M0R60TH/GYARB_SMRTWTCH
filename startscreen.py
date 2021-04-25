from m5stack import * #import m5stack library for Core2 module
from m5stack_ui import * #import m5stack_ui library to be able to send code between UIFlow program and software on Core2  
from uiflow import * #import the UIFlow library
import wifiCfg #import wifiCfg library to be able to connect to wifi

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)


wifiCfg.doConnect('SSID', 'PASSWORD')
time_start = M5Label('Retrieving time', x=5, y=47, color=0x000, font=FONT_MONT_26, parent=None)
To_Menu = M5Btn(text='Press to continue', x=35, y=140, w=250, h=70, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
time_topscreen = M5Label('Retrieving time', x=155, y=4, color=0x000, font=FONT_MONT_14, parent=None)
Battery_percentage = M5Label('%', x=83, y=4, color=0x000, font=FONT_MONT_12, parent=None)
line0 = M5Line(x1=0, y1=25, x2=320, y2=25, color=0x000, width=1, parent=None)

def To_Menu_pressed():
  # global params
  pass
To_Menu.pressed(To_Menu_pressed)


lcd.rect(80, 2, 60, 20, color=0x000000)
lcd.rect(139, 7, 5, 10, color=0x000000)
while True:
  time_start.set_text(str(rtc.printRTCtime()))
  time_topscreen.set_text(str(rtc.printRTCtime()))
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
