from logging import getLogger, NullHandler
logger = getLogger('takanami')
logger.addHandler(NullHandler())

__version__ = '0.0.0'

