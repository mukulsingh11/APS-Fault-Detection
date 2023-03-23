from sensor.logger import logging
from sensor.exception import SensorException
import os,sys


def test_logger_and_exception():
    try:
        logging.info("Starting the test logger and exception")
        result =3/0
        print(result)
        logging.info(" Ending point of the test logger and exception")
    except Exception as e:
        logging.info(str(e))
        raise SensorException (e,sys)
    
if __name__=="__main__":
    try:
        test_logger_and_exception()
    except Exception as e:
        print(e)
