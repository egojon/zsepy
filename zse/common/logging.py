import logging

logging.basicConfig(format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s", level=logging.DEBUG)


def getLogger():
    return get_logger()


def get_logger():
    logger = logging.getLogger('zse')
    return logger
