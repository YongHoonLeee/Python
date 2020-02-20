import logging

logging.basicConfig(filename='test.log', level=logging.INFO)

logging.critical('critical')
logging.error('error')
logging.warning('warning')
logging.info('info')
logging.debug('debug')
logging.info('info %s %s', 'test1', 'test2')
