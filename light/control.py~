# coding=utf-8
from query import getDeviceData,getBlubData,getSpeakerData
import time
import RPi.GPIO as GPIO


USING_PIN = 11

def changeDutyTo(p,val):
    if(val>=0 and val <=100):
        p.ChangeDutyCycle(val)
        print "Change Bulb-value to [%d]" % val




if(__name__=="__main__"):
    #initial pin
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(USING_PIN, GPIO.OUT)

    p = GPIO.PWM(12, 50) # 将12号引脚初始化为PWM实例 ，频率为50Hz
    p.start(0) # 开始脉宽调制，参数范围为： (0.0 <= dc <= 100.0)


    while(True):
        time.sleep(1)
        res = getDeviceData()
        changeDutyTo(p,getBlubData(res))
