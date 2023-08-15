#!/usr/bin/python3

# Script Name:                 401-ops-class26.py               
# Class Name:                  Ops 401d8
# Author Name:                 David Siebert 
# Date of latest revision:     14AUG2023
# Event logging tool Part 1 of 3. 


# import libraries 
import logging 
import os 


# confiogure the basic of the logger , formatting messages filemode write
logging.basicConfig(filename="demo.log", format='%(asctime)s %(message)s', filemode='w')

#creating log onbject
log = logging.getLogger("my_logger")
 
#setting the level of message to log
log.setLevel(logging.WARNING)

#generate a set of test log messages
log.debug("Harmless Debug ")
log.info("An Information Message")
log.warning("A WARNING")
log.error("AN ERROR")
log.critical("Worst Case Scenario")

def do_things():
    log.debug("doing things")

do_things():