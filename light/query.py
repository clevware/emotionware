
import requests
import json

DEVICE_URL = "http://wzhere.cn:7036/get_device_list"
MSG_URL = "http://wzhere.cn:7036/get_message"


def getDeviceData():
    res = requests.get(DEVICE_URL)
    res_json = json.loads(res.text)
    return res_json

def getBlubData(device_json):
    for d in device_json:
        if('type' in d and d['type']=="bulb"):
            return d['state']

def getSpeakerData(device_json):
    for d in device_json:
        if('type' in d and d['type']=="speaker"):
            return d['state']

def getMessage():
    res = requests.get(MSG_URL)
    res_json = json.loads(res.text)
    if(res_json['flag']==1):
        return res_json['message']
    else:
        return ''

def getMusicCommand(msg):
    if(msg[0:10]=="MUSIC:PLAY"):
        return 1
    if(msg[0:10]=="MUSIC:NEXT"):
        return 2
    if(msg[0:11]=="MUSIC:PAUSE"):
        return 3

    return 0



if(__name__=="__main__"):
    import time

    while(True):
        res = getDeviceData()
        time.sleep(1)
        print "Bulb state:",getBlubData(res)
        print "Message:",getSpeakerData(res)
        print getMessage()