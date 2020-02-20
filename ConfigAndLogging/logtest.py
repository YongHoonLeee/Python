import logging

logging.basicConfig(filename='ConfigAndLogging/test.log', level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

h = logging.FileHandler('ConfigAndLogging/test.log')
logger.addHandler(h)


def do_something():
    logging.info('from logtest info')
    logging.debug('from logtest debug')


do_something()
