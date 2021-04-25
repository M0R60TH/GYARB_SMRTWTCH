start_stop_count = None #create variable start_stop_count and set it to none
resetcount = None #create variable resetcount and set it to none
sec = None #create variable sec and set it to none


   #create label named seconds for unit sec and set label’s preferences
seconds = M5Label('00', x=134, y=21, color=0x000, font=FONT_MONT_48, parent=None)
   #create button named start_stop for start/stop button and set button’s preferences
start_stop = M5Btn(text='start/stop', x=123, y=96, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
   #create button named reset for reset button and set button’s preferences
reset = M5Btn(text='reset', x=125, y=177, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)

from numbers import Number #import numbers

def start_stop_pressed(): #when start_stop button is pressed
  global start_stop_count, resetcount, sec #import variable from outside function
  start_stop_count = (start_stop_count if isinstance(start_stop_count, Number) else 0) + 1 #add +1 on start_stop_count
  pass
start_stop.pressed(start_stop_pressed) #start_stop button pressed

def reset_pressed(): #when reset button is pressed
  global start_stop_count, resetcount, sec #import variable from outside function
  resetcount = (resetcount if isinstance(resetcount, Number) else 0) + 1 #add +1 on resetcount when pressed
  pass
reset.pressed(reset_pressed) #reset button pressed

sec = 0 #set variable sec to 0
start_stop_count = 0 #set variable start_stop_count to 0
resetcount = 0 #set variable resetcount to 0
while True: #while loop
  if start_stop_count % 2 == 1: #if start_stop_count is an odd value then:
    sec = (sec if isinstance(sec, Number) else 0) + 1 #change variable sec by 1
    resetcount = 0
    wait(1) #wait 1 second
  if resetcount % 2 == 1: #if resetcount is an odd value then:
    start_stop_count = 0
    sec = 0
    wait(1)
  seconds.set_text(str(sec)) #print out value of sec on Label namned seconds
  wait_ms(2) #wait 2ms, automatic when using UIFlow and loop
