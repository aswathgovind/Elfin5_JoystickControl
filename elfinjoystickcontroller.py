import time
import pygame
from ElfinRobotMovementHTIC import *

class Cmd(object):
    def __init__(self):
        self.reset()

    def reset(self):
        self.axis0 = 0
        self.axis1 = 0
        self.axis2 = 0 
        self.axis3 = 0
        self.axis4 = 0
        self.axis5 = 0 
        self.btn0 = 0
        self.btn1 = 0
        self.btn2 = 0
        self.btn3 = 0
        self.btn4 = 0
        self.btn5 = 0
        self.btn6 = 0
        self.btn7 = 0
        self.btn8 = 0
        self.btn9 = 0
        self.hat0 = 0

class Service(object):
    def __init__(self, robot):
        self.joystick = None
        self.robot = robot
        self.cmd = Cmd()

    def init_joystick(self):
        pygame.init()
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()
    
    def test(self,wet):
        print(wet)
    
    def loop(self):
        air = False
        while True:
            self.cmd.reset()
            pygame.event.pump()
            
            for i in range(0, self.joystick.get_numaxes()):
                val = self.joystick.get_axis(i)
                if abs(val) < 0.2:
                    val = 0
                tmp = "self.cmd.axis" + str(i) + " = " + str(val)
                if val != 0:
                    exec(tmp)
                
            for i in range(0, self.joystick.get_numhats()):
                val = self.joystick.get_hat(i)
                tmp = "self.cmd.hat" + str(i) + " = " + str(val)
                exec(tmp)
            

            for i in range(0, self.joystick.get_numbuttons()):
                if self.joystick.get_button(i) != 0:
                    tmp = "self.cmd.btn" + str(i) + " = 1"
                    exec(tmp)

            if self.cmd.btn1:
                #toggle IO
                air = not air
                stoprobot(self.robot)

            #(0:X,1:Y,2:Z,3:A,4:B,5:C)
            #0=negative;1=positive

                                      
            if self.cmd.btn0 and self.cmd.hat0 == (0, 1):
                print("value from the hat is,self.cmd.btn0",self.cmd.hat0,self.cmd.btn0)
                LongJogL(self.robot,2,1)
            elif self.cmd.btn0 and self.cmd.hat0 == (0, -1):
                print("value from the hat is,self.cmd.hat0",self.cmd.hat0,self.cmd.btn0)
                LongJogL(self.robot,2,0)
            elif self.cmd.hat0 == (0, 1):
                print("value from the hat is",self.cmd.hat0)
                self.test("test")
                LongJogL(self.robot,1,0)
            elif self.cmd.hat0 == (0, -1):
                print("value from the hat is",self.cmd.hat0)
                LongJogL(self.robot,1,1)
            elif self.cmd.hat0 == (1, 0):
                print("value from the hat is",self.cmd.hat0)
                LongJogL(self.robot,0,0)
            elif self.cmd.hat0 == (-1, 0):
                print("value from the hat is",self.cmd.hat0)
                LongJogL(self.robot,0,1)
            elif self.cmd.axis0 > 0.5 :
                LongJogL(self.robot,3,1)
                print("movement in axis0")
            elif self.cmd.axis0 < -0.5:
                LongJogL(self.robot,3,0)
                print("movement in axis0")
            elif self.cmd.axis1 > 0.5:
                 LongJogL(self.robot,4,1)
            elif self.cmd.axis1 < -0.5:
                 LongJogL(self.robot,4,0)
            elif self.cmd.axis2 > 0.5:
                LongJogL(self.robot,5,1)
            elif self.cmd.axis2 < -0.5:
                LongJogL(self.robot,5,0)
            else:
                stoprobot(self.robot)        

    def close(self):
        if self.joystick:
            self.joystick.quit()


if __name__ == "__main__":

    s = connect('172.16.101.34')
    
    service = Service(s)
    service.init_joystick()
    try:
        service.loop() 
    finally: 
        service.close()
