import logging
import time

# logging.warning('Watch out!') # prints message to console
# logging.info('I told you so') # doesn't print cuz default level is WARNING

# Logging to a file
# logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')
# logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

# Logging to a file and with time'
# getattr(logging, loglevel.upper()) returns the value passed to basicConfig() via the level arg
logging.basicConfig(
    filename='example.log',
    encoding='utf-8',
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.DEBUG,
    datefmt='%Y-%m-%d %H:%M:%S'
)
logging.info('Info message #1')

time.sleep(2)

logging.info('Info message #2')

time.sleep(2)

logging.debug('Debug message #1')

time.sleep(2)

logging.error('Error message #1')

time.sleep(2)

logging.warning('Warning message #1')

time.sleep(2)

logging.critical('Critical message #1')

