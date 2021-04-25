from m5stack import * #import m5stack library for Core2 module
from m5stack_ui import * #import m5stack_ui library to be able to send code between UIFlow program and software on Core2  
from uiflow import * #import the UIFlow library
import wifiCfg #import wifiCfg library to be able to connect to wifi

screen = M5Screen() #set screen to the screen on module
#clean screen and set it to white color
screen.clean_screen()  
screen.set_screen_bg_color(0xFFFFFF)


wifiCfg.doConnect('SSID', 'PASSWORD') #choose what netowrk to connect to by entering its SSID and password
#create button namned To_Menu and when pressed it will change to the menu section, set the button settings
To_Menu = M5Btn(text='Press to continue', x=35, y=140, w=250, h=70, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
#create labels for display of time on startscreen, top of the screen and the battery status and set their settings
time_start = M5Label('Retrieving time', x=5, y=47, color=0x000, font=FONT_MONT_26, parent=None)
time_topscreen = M5Label('Retrieving time', x=155, y=4, color=0x000, font=FONT_MONT_14, parent=None)
Battery_percentage = M5Label('%', x=83, y=4, color=0x000, font=FONT_MONT_12, parent=None)
#create line top of screen so it creates a top section for time and battery status
line0 = M5Line(x1=0, y1=25, x2=320, y2=25, color=0x000, width=1, parent=None)

def To_Menu_pressed(): #function for To_Menu button, code at the moment has no menu but the button is placed for future coding 
  # global params
  pass
To_Menu.pressed(To_Menu_pressed) #determine when To_Menu button is pressed

#create rectangles and placed them so it creates a battery icon
lcd.rect(80, 2, 60, 20, color=0x000000)
lcd.rect(139, 7, 5, 10, color=0x000000)
while True: #while loop
  #print the RTC time retreived through internet on both time labels
  time_start.set_text(str(rtc.printRTCtime())) 
  time_topscreen.set_text(str(rtc.printRTCtime()))
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
  wait_ms(2)
