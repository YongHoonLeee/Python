import logging

formatter = '%(asctime)s :%(levelnames)s : %(message)s'
logging.basicConfig(level=logging.INFO, format=formatter)

logging.critical('critical')
logging.error('error')
logging.warning('warning')
logging.info('info')
logging.debug('debug')
