from logging import getLogger, INFO, DEBUG
logger = getLogger(__name__)

from takanami.exception import ConfiturationError
import os

class ConfigurationBase:
    def __getattr__(self, key):
        try:
            return os.environ[key.upper()]
        except KeyError:
            raise ConfiturationError(str(key) + ' is not Confiturate.')

class Configuration:
    dynamodb_table_name = 'infra.status'
    dynamodb_primary_key_name = 'status_key'
    dynamodb_main_key_name = 'takanami_stack'

Conf = Configuration()
