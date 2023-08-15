#!/usr/bin/python3

# Script Name:                 401-ops-class27.py               
# Class Name:                  Ops 401d8
# Author Name:                 David Siebert 
# Date of latest revision:     15AUG2023
# Event logging tool Part 2 of 3.  

#import Libraries 
import logging, time, os 
from logging.handlers import RotatingFileHandler

# create logger object
logger =logging.getLogger('my_logger')



# confiogure the basic of the logger , formatting messages filemode write
logging.basicConfig(filename="my_logs.log", format='%(asctime)s %(message)s', filemode='w')

#setting the level of message to log
logger.setLevel(logging.WARNING)

#generate a set of test log messages
log.debug("Harmless Debug ")
log.info("An Information Message")
log.warning("A WARNING")
log.error("AN ERROR")
log.critical("Worst Case Scenario")

# Create the handler
handler = RotatingFileHandler('mylogs.log', maxBytes= 20, backupCount=3)

#tell PY to use the two together ( use the handler ) 
logger.addHandler(handler)

#testing (while true send the message every second, must set level -formating) 
while True:
  time.sleep(1)
  logger.info("insert ative message here")
