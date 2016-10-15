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
    def __init__(self,id="",serverURL="http://cleverhome.mybluemix.net",pin=17):
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
            data=data,
        )
        print res
        res = json.loads(res)

        if(res['value']>0):
            self.light.on()
        else:
            self.light.off()


if(__name__=="__main__"):

    testone = Light()

    while True:
        testone.getLightState()
        time.sleep(2)
