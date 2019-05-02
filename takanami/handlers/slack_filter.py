from logging import getLogger, INFO, DEBUG
logger = getLogger(__name__)
logger.setLevel(DEBUG)

import json
import os
import boto3

from takanami.kishinami import Kishinami
from takanami.dynamodb import getStack
from takanami.lambda_controll import invoke

def main(event, context):
    kishinami = Kishinami('kishinami')

    kishinami.shock([45,200,0])

    stack = getStack()
    item = stack.stack()
    item['slack'][event['channel']] = event
    stack.save(item)

    invoke('notice_check')
    return {}

if __name__ == '__main__':
    main({'channel':'testchannel','ts':0}, {})
