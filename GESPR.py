#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from pcms.openvino_models import Yolov8, HumanPoseEstimation
from open_manipulator_msgs.srv import SetJointPosition, SetJointPositionRequest
from open_manipulator_msgs.srv import SetKinematicsPose, SetKinematicsPoseRequest
import numpy as np
from geometry_msgs.msg import Twist
from pcms.pytorch_models import *
from pcms.openvino_yolov8 import *
import math
import time
from mr_voice.msg import Voice
from std_msgs.msg import String
from sensor_msgs.msg import Imu
from tf.transformations import euler_from_quaternion
from gtts import gTTS
from playsound import playsound
import requests
import json


def callback_voice(msg):
    global s
    s = msg.text

def say(g):
    os.system(f'espeak "{g}"')
    rospy.loginfo(g)

if __name__ == "__main__":
    rospy.init_node("demo")
    rospy.loginfo("demo node start!")
    '''
    print("speaker")
    rospy.Subscriber("/voice/text", Voice, callback_voice)
    publisher_speaker = rospy.Publisher("/speaker/say", String, queue_size=10)
    print("load")'''
    for i in range(3):
        s1=input("The sentence is: ")
        api_url = "http://192.168.50.147:8888/Fambot"
        my_todo = {"Question1":"None","Question2":"None","Question3":"None","Steps":0,"Voice":s1}
        response = requests.post(api_url, json=my_todo, timeout=2.5)
        result = response.json()
        print("post",result)
        
        while True:
            r = requests.get("http://192.168.50.147:8888/Fambot",timeout=2.5)
            response_data = r.text
            dictt = json.loads(response_data)
            if dictt["Steps"] == 1:
                break
            pass
            time.sleep(2)
        Q1=dictt["Question1"]
        Q2=dictt["Question2"]
        Q3=dictt["Question3"]
        print(Q1)
        print(Q2)
        print(Q3)
        
        
#Get a detergent from the tray B and bring it to Adam in the living room

        
