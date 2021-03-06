import requests,json
from uuid import uuid4
from gpiozero import LED
import time

class Light():

    id = str()
    serverURL = str()
    session = requests.session()
    light = None

    #inti whit a id
    def __init__(self,id="",serverURL="http://clevho.mybluemix.net/light-brightness",pin=17):
        if(len(id)>0):
            self.id = id
        else:
            self.id=uuid4()
        if(len(serverURL)>0):
            self.serverURL = serverURL
        if(pin!=0):
            self.light = LED(pin)

    # send a request to get light state
    def getLightState(self):

        data={
            'id':self.id,
        }

        res=self.session.post(
            url=self.serverURL,
            cookies=data,
            data=data,
        )
        print res.status_code
        print "[ "+res.text+" ]\n"
        if(res.status_code==200):
            res = json.loads(res.text)
            if(res['value']>0):
                self.light.on()
            else:
                self.light.off()


if(__name__=="__main__"):
    testone = Light(pin=17,id="1")
    while True:
        try:
            testone.getLightState()
        except Exception,e:
            print e
