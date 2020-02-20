import logging

# logging.basicConfig(level=INFO filename='./test.log')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class NoPassFilter(logging.Filter):
    def filter(self, record):
        log_message = record.getMessage()
        return 'password' not in log_message


logger.addFilter(NoPassFilter())
logger.debug('debug')
h = logging.FileHandler('ConfigAndLogging/test.log')
logger.addHandler(h)
logger.info('nickname : yonghoon')
logger.info('password : yonghoon')
logger.debug('wowowowo password')
logger.debug('wowowowo pasword')

