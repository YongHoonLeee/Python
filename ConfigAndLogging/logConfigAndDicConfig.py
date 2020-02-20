import logging
import logging.config


logging.config.fileConfig('Python/ConfigAndLogging/logging.ini')
logger = logging.getLogger(__name__)
logger.debug('debug log')
logger.info('info log')
logger.warning('warning log')
logger.error('error log')
logger.critical('critical log')
