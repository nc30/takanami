from logging import getLogger
logger = getLogger(__name__)

import boto3
import json
client = boto3.client('lambda')

def invoke(FunctionName, payload={}):
    client.invoke(
        FunctionName=FunctionName,
        InvocationType='Event',
        Payload=json.dumps(payload).encode('utf-8')
    )
