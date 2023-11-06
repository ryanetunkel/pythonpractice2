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
# logging.basicConfig(
#     filename='example.log',
#     encoding='utf-8',
#     format='%(asctime)s %(levelname)-8s %(message)s',
#     level=logging.DEBUG,
#     datefmt='%Y-%m-%d %H:%M:%S'
# )
# logging.info('Info message #1')

# time.sleep(2)

# logging.info('Info message #2')

# time.sleep(2)

# logging.debug('Debug message #1')

# time.sleep(2)

# logging.error('Error message #1')

# time.sleep(2)

# logging.warning('Warning message #1')

# time.sleep(2)

# logging.critical('Critical message #1')


# assuming loglevel is bound to the string value obtained from the
# command line argument. Convert to upper case to allow the user to
# specify --log=DEBUG or --log=debug
# numeric_level = getattr(logging, loglevel.upper(), None)
# if not isinstance(numeric_level, int):
#     raise ValueError('Invalid log level: %s' % loglevel)
# logging.basicConfig(level=numeric_level, ...)

# Allows the above code to reset example.log each time
# logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)


# Logging from multiple modules
# import mylib

# def main():
#     logging.basicConfig(filename='myapp.log', level=logging.INFO)
#     logging.info('Started')
#     mylib.do_something()
#     logging.info('Finished')

# if __name__ == '__main__':
#     main()


# Logging variable data
# logging.warning('%s before you %s', 'Look', 'leap!') # C vibes


# Changing the format of displayed messages
# logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
# logging.debug('This message should appear on the console')
# logging.info('So should this')
# logging.warning('And this, too')


# Dispalying date/time in messages
# logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p') # %(asctime)s displays date and time of an event, datefmt formats the date
# logging.warning('is when this event was logged.')