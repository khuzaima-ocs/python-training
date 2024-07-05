import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger("xTreme-Logger")
handler = logging.FileHandler('my_logs.log')
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(levelname)s - %(asctime)s :  %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.debug("This is debug message")
logger.info("This is info message")
logger.warning("This is warning message")
logger.error("This is error message")
logger.critical("This is critical message")