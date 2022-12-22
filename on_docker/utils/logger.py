import sys
sys.dont_write_bytecode = True

import os
import warnings
import logging

loggers = {}


def get_logger(name: str = __name__, ignore_future_warning: bool = True):
    global loggers

    if loggers.get(name):
        return loggers.get(name)

    logger = logging.getLogger(name)

    # log format
    formatter = logging.Formatter('%(asctime)s %(funcName)s:%(lineno)d <%(levelname)s> %(message)s')

    if "LOG_FILE" in os.environ:
        # add file handler
        file_handler = logging.FileHandler(os.environ["LOG_FILE"])
        file_handler.setLevel(logging.NOTSET)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.propagate = False
    else:
        # add console handler
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.NOTSET)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
        logger.propagate = False

    # logger set level
    if "LOG_LEVEL" in os.environ:
        if os.environ["LOG_LEVEL"].upper() == "NOTSET":
            logger.setLevel(logging.NOTSET)
        elif os.environ["LOG_LEVEL"].upper() == "DEBUG":
            logger.setLevel(logging.DEBUG)
        elif os.environ["LOG_LEVEL"].upper() == "INFO":
            logger.setLevel(logging.INFO)
        elif os.environ["LOG_LEVEL"].upper() == "WARNING" or os.environ["LOG_LEVEL"].upper() == "WARN":
            logger.setLevel(logging.WARNING)
        elif os.environ["LOG_LEVEL"].upper() == "ERROR":
            logger.setLevel(logging.ERROR)
        elif os.environ["LOG_LEVEL"].upper() == "CRITICAL":
            logger.setLevel(logging.CRITICAL)
        else:
            logger.setLevel(logging.INFO)
    else:
        logger.setLevel(logging.INFO)

    # future warning don't output.
    if ignore_future_warning:
        warnings.simplefilter(action='ignore', category=FutureWarning)

    loggers[name] = logger

    return logger


def test_logging():
    logger = get_logger()
    logger.debug("test")
    logger.info("info")
    logger.warning("warn")
    logger.error("error")
    logger.critical("critical")


if __name__ == '__main__':
    test_logging()

