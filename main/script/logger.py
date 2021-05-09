import logging
import os
import sys
#directory
log_dir = '/app/logs'
if not os.path.exists(log_dir):
    os.mkdir(log_dir)

def makelog(name=None):
    logger = logging.getLogger(name)
    formatter = logging.Formatter('[%(asctime)s:%(name)s] %(filename)s line:%(lineno)d [%(levelname)s] %(message)s')
    logger.setLevel(logging.DEBUG)

    from logging.handlers import TimedRotatingFileHandler
    fileHandler = TimedRotatingFileHandler(filename='/app/logs/log.log', when='midnight', interval=1, encoding='utf-8')
    fileHandler.setFormatter(formatter)
    fileHandler.suffix = '%Y%m%d'
    fileHandler.setLevel(logging.DEBUG)
    logger.addHandler(fileHandler)
    return logger
"""
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(formatter)
streamHandler.setLevel(logging.DEBUG)
logger.addHandler(streamHandler)
"""
