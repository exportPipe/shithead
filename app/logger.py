import logging
import os
from logging.handlers import TimedRotatingFileHandler
import sys


def setup_logger():
    log_dir = "data/logs/"
    os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger("uvicorn.error")
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    log_file = os.path.join(log_dir, "server.log")
    fh = TimedRotatingFileHandler(log_file, when="midnight", interval=1, backupCount=30)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger

