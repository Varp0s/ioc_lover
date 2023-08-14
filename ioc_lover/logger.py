import logging
from logging.handlers import RotatingFileHandler

def setup_logger():
    log = logging.getLogger("ioc_search")
    log.setLevel(logging.DEBUG)

    log_file = "./data/ioc_search.log"
    file_handler = RotatingFileHandler(log_file, maxBytes=100000, backupCount=5)
    file_handler.setLevel(logging.DEBUG)
    
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    log.addHandler(file_handler)
    log.addHandler(console_handler)

    return log

log = setup_logger()
