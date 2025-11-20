import logging

LOG_FORMAT = "%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d | %(message)s"

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)  

    if not logger.handlers:
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        
        formatter = logging.Formatter(LOG_FORMAT)
        ch.setFormatter(formatter)
        
        logger.addHandler(ch)

    return logger
