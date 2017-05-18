# coding=utf-8
from query import getDeviceData,getMessage
from control import changeDutyTo,getBlubData,espeak
import RPi.GPIO as GPIO
import time


if(__name__=="__main__"):
    USING_PIN = 12

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(USING_PIN, GPIO.OUT)

    p = GPIO.PWM(USING_PIN, USING_PIN) # 将12号引脚初始化为PWM实例 ，频率为50Hz
    p.start(0) # 开始脉宽调制，参数范围为： (0.0 <= dc <= 100.0)

    while(True):
        time.sleep(1)
        res = getDeviceData()
        changeDutyTo(p,getBlubData(res))


        message = getMessage()
        if(len(message)>0):
            espeak(message)
