import requests,json

class Client():

    id = str()
    serverURL = str()
    session = requests.session()

    #inti whit a id
    def __init__(self,id,serverURL="http://cleverhome.mybluemix.net"):
        if(len(id)>0):
            self.id = id
        if(len(serverURL)>0):
            self.serverURL = serverURL

    # send a request to get light state
    def getLightState(self,serverURL):

        data={
            'id':self.id,
        }

        res=self.session.post(
            url=self.serverURL,
            data=data,
        )
        res = json.loads(res)