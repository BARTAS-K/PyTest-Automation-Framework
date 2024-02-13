import inspect
import logging


class Logger:

    def getLogger(self):
        testName = inspect.stack()[2][3]
        logger = logging.getLogger(testName)
        fileHandler = logging.FileHandler("logFile.log")
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger