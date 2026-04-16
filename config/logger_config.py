import logging
from .pathlib_config import get_scanner_log_path

def setup_logger():
    """setup logger for print info+ and save debug+ in .log file"""

    log_file = get_scanner_log_path()

    #creet object && set level

    logger = logging.getLogger("pynmap")
    logger.setLevel(logging.DEBUG)

    #file handler

    file_handler = logging.FileHandler(log_file,encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s')
    file_handler.setFormatter(file_format)


    #console handler

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_format = logging.Formatter('%(levelname)s: %(message)s')
    console_handler.setFormatter(console_format)

    #add hanlers

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

if __name__ == "__main__":
    setup_logger()
