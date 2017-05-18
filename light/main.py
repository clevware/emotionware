# coding=utf-8
from query import getDeviceData,getMessage,getMusicCommand
from control import changeDutyTo,getBlubData,espeak,music_pause,music_play,music_next
import RPi.GPIO as GPIO
import time


if(__name__=="__main__"):
    USING_PIN = 12

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(USING_PIN, GPIO.OUT)

    p = GPIO.PWM(USING_PIN, 100) # 将12号引脚初始化为PWM实例 ，频率为100Hz
    p.start(0) # 开始脉宽调制，参数范围为： (0.0 <= dc <= 100.0)

    while(True):
        time.sleep(1)
        res = getDeviceData()
        brightness = float(getBlubData(res))
        print "Bulb state:",brightness
        changeDutyTo(p,brightness)


        message = getMessage()
        if(len(message)>0):
            print "New Message:",message
            if(getMusicCommand(message)==0):
                espeak(message)
            elif(getMusicCommand(message)==1):
                music_next()
            elif (getMusicCommand(message) == 2):
                music_next()
            elif(getMusicCommand(message)==3):
                music_pause()