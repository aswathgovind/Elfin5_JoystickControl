from pynput.keyboard import Key, Listener
from ElfinRobotMovementHTIC import *

s = connect('172.16.101.34')


#(0:X,1:Y,2:Z,3:A,4:B,5:C)
#0=negative;1=positive

def on_press(key):
    if(key == Key.left):
        print("left arrow")
        LongJogL(s,0,0)
    elif(key == Key.right):
        print("right arrow")
        LongJogL(s,0,1)
    elif(key == Key.down):
        print("down arrow")
        LongJogL(s,1,0)
    elif(key == Key.up):
        print("up arrow")
        LongJogL(s,1,1)
    elif(key == Key.page_up):
        print("page_up")
        LongJogL(s,2,1)
    elif(key == Key.page_down):
        print("page_down")
        LongJogL(s,2,0)
    elif(key == Key.ctrl_l):
        print("ctrl_l")
        LongJogL(s,3,1)
    elif(key == Key.ctrl_r):
        print("ctrl_r")
        LongJogL(s,3,0)
    elif(key == Key.shift_l):
        print("shift_l")
        LongJogL(s,4,0)
    elif(key == Key.shift_r):
        print("shift_r")
        LongJogL(s,4,1)
    elif(key == Key.alt_l):
        print("alt_l")
        LongJogL(s,5,0)
    elif(key == Key.alt_r):
        print("alt_r")
        LongJogL(s,5,1)
   
def on_release(key):
    stoprobot(s)
    print("stopped robot")
    if key == Key.esc:
        return False

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
