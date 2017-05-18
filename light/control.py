# coding=utf-8
from query import getDeviceData,getBlubData,getSpeakerData,getMessage
import time
import RPi.GPIO as GPIO
import os
import random

USING_PIN = 11
MP3_DIRECTORY = "/home/pi/Desktop/King/mp3/"

def getMP3List():
    mp3_list = os.listdir(MP3_DIRECTORY)
    random.shuffle(mp3_list)
    return mp3_list


def music_pause():
    os.system("pkill mplayer")


def music_play(name):
    music_pause()
    os.system("mplayer %s" % (MP3_DIRECTORY+name))

def music_next():
    mp3_list = getMP3List()
    choose = random.randint(len(mp3_list))
    music_play(mp3_list[choose])



def changeDutyTo(p,val):
    if(val>=0 and val <=100):
        p.ChangeDutyCycle(val)
        print "Change Bulb-value to [%d]" % val

def espeak(message):
    os.system("espeak '%s'" % message)


def mpayer(name):
    os.system("mplayer '%s'" % name)

if(__name__=="__main__"):
    #initial pin
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(USING_PIN, GPIO.OUT)

    p = GPIO.PWM(USING_PIN, 12) # 将12号引脚初始化为PWM实例 ，频率为50Hz
    p.start(0) # 开始脉宽调制，参数范围为： (0.0 <= dc <= 100.0)




    while(True):
        time.sleep(1)
        res = getDeviceData()
        changeDutyTo(p,getBlubData(res))


        message = getMessage()
        if(len(message)>0):
            espeak(message)
