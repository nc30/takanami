from logging import getLogger
logger = getLogger(__name__)

import boto3
import json

client = boto3.client('iot-data')

class Kishinami:
    def __init__(self, thingName):
        self.thingName = thingName

    def changeState(self, state):
        self.changeThingStatus(state=state)

    def changeThingStatus(self, **kwargs):
        desired = {}
        desired.update(kwargs)

        response = client.update_thing_shadow(
           thingName=self.thingName,
           payload=json.dumps({
               "state": {
                   "desired": desired
               }
           })
        )

    def shock(self, color=[200, 20, 0]):
        r = client.publish(
            topic='cmnd/' + self.thingName + '/shock',
            qos=0,
            payload=json.dumps({"color":color})
        )

if __name__ == '__main__':
    kishinami = Kishinami('kishinami')
    import time
    kishinami.shock()
    time.sleep(1)
    kishinami.shock([0,10,255])
    time.sleep(1)
    kishinami.changeState('siren')
    time.sleep(5)
    kishinami.changeState('warning')
    time.sleep(5)
    kishinami.changeState('normal')
