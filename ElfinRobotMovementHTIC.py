import math
from math import *
import math3d as m3d
import numpy as np
import time
import socket 
import os
# import tqdm


# #-------------------General Modules
import socket
import numpy as np
import os
import math


# #-------------------Math and Robot Modules
from scipy.spatial.transform import Rotation as R
import matplotlib.pyplot as plt


# #-------------------Core Robotic Modules
ip = "192.168.0.10"
port = int("10003")



#---------------------------------------------------------------------------------------------------------
#Modules to Make Motion  of the Robot with respect to the Robot



def connect(ip = "192.168.0.10", port = 10003):
    """Connect to the robot

    Args:
        ip ([String]): [192.168.0.10]
        port ([Int]): [10003]

    Returns:
        [Object]: [soccet communication s]
    """
    try:
        s = socket.socket()
        s.connect((ip, int(port)))
        print('robot connected succesfully to')
        print('ip - {}'.format(ip), '\n', 'port - {}'.format(port))
        return s
    except Exception as e:
        print(e)
        print("cant retrive the Actual Position of the Robot")


def LongJogL(s, axis,direction, port=10003, robotID=0):
    """[Move the robot using Joint Values]

    Args:
        s ([Object]): [Robot TCP Connection]
        angles ([List of Floats]): [Joint angles]
        port (int, optional): [Port you got connected to]. Defaults to 10003.
        robotID (int, optional): [The unique identifier of the robot]. Defaults to 0.
    """
    try:
        # x, y, z, rx, ry, rz = tuple(pose)
        data = str("LongJogL,{},{},{},;\n".format(robotID, axis,direction))
        
        # print(data)
        data = data.encode()
        s.send(data)
        result = s.recv(port).decode()
        # print('result is',result)
        # cut = result.split(',')
        # if(cut[1] == "OK"):
        #     while 1:
        #         s.send("ReadRobotState,0,;".encode())
        #         result = s.recv(port).decode()
        #         cut = result.split(',')
        #         # print('cut',cut)
        #         if(cut[1] == "OK" and cut[2] == "0"):
        #             break
        # elif(cut[1] == "Fail"):
        #     print(result)
    except Exception as e:
        print(e)
        print("cant retrive the Actual Position of the Robot")

def stoprobot(s, port=10003, robotID=0):

    try:
        data = str("GrpStop,0,;")
        # print(data)
        data = data.encode()
        s.send(data)
        result = s.recv(port).decode()
        # print('result is',result)
        cut = result.split(',')
        if(cut[1] == "OK"):
            while 1:
                s.send("ReadRobotState,0,;".encode())
                result = s.recv(port).decode()
                cut = result.split(',')
                # print('cut',cut)
                if(cut[1] == "OK" and cut[2] == "0"):
                    break
        elif(cut[1] == "Fail"):
            print(result)
    except Exception as e:
        print(e)
        print("cant stop robot")
       
        
