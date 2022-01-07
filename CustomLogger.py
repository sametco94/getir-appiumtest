import inspect
import logging

import allure


def customlogger():
    logname = inspect.stack()[1][3]
    logger = logging.getLogger(logname)
    logger.setLevel(logging.DEBUG)
    filehandler = logging.FileHandler("C:/Users/esame/PycharmProjects/reports/Code2Lead.log", mode='a')
    filehandler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s',
                                  datefmt='%d/%m/%y %I:%M:%S %p %A')

    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    return logger


def allurelogs(text):
    with allure.step(text):
        pass
