import requests
import json

def getDeviceData():
    res = requests.get("http://wzhere.cn:7036/get_device_list")
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
    res = requests.get("http://wzhere.cn:7036/get_message")
    res_json = json.loads(res)
    if(res_json['flag']==1):
        return res_json['message']
    else:
        return ''

if(__name__=="__main__"):
    res = getDeviceData()

    print getBlubData(res)
    print getSpeakerData(res)