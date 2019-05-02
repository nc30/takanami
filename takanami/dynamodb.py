from logging import getLogger
logger = getLogger(__name__)

from takanami.config import Conf
import boto3
import time
import hashlib
import json

dynamo = boto3.resource('dynamodb')

def getStack():
    return Stack(
        table_name=Conf.dynamodb_table_name,
        primary_key=Conf.dynamodb_primary_key_name,
        main_key=Conf.dynamodb_main_key_name
    )


class Stack:
    def __init__(self, table_name, primary_key, main_key):
        self.primary_key = primary_key
        self.main_key = main_key
        self.table_name = table_name

        self.table = dynamo.Table(table_name)
        self.item = None

    def stack(self, force=False):
        if self.item is None or force:
            self.item = self._getItem()

        return self.item

    def _getItem(self):
        r = self.table.get_item(
            Key={
                self.primary_key: self.main_key
            }
        )
        item = r.get('Item', {
                self.primary_key: self.main_key,
                'slack': {
                },
                'github': {
                },
                'change_digest': '',
            }
        )
        return item

    def save(self, item, changeTime=True):
        self.item = item
        self.item['last_update'] = int(time.time())

        self._save(self.item)

    def _save(self, item):
        self.table.put_item(
            Item=item
        )

    def isChange(self, notices):
        digest = hashlib.sha224(json.dumps(notices).encode()).hexdigest()
        return self.stack()['change_digest'] != digest
