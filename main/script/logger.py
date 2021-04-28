import logging
import os
log_dir = './logs'
if not os.path.exists(log_dir):
    os.mkdir(log_dir)

logger = logging.getLogger(__name__)
formatter = logging.Formatter(u'%(asctime)s [%(levelname)8s] %(message)s')
logger.setLevel(logging.DEBUG)


from logging.handlers import TimedRotatingFileHandler
fileHandler = TimedRotatingFileHandler(filename=log_dir+'/error.log', when='midnight', interval=1, encoding='utf-8')
fileHandler.setFormatter(formatter)
fileHandler.suffix = '%Y%m%d'
fileHandler.setLevel(logging.ERROR)
logger.addHandler(fileHandler)

streamHandler = logging.StreamHandler()
streamHandler.setFormatter(formatter)
streamHandler.setLevel(logging.DEBUG)
logger.addHandler(streamHandler)


