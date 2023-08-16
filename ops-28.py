#!/usr/bin/python3

# Script Name:                 401-ops-class26-7-oswalkencrypt-logging.py              
# Class Name:                  Ops 401d8
# Author Name:                 David Siebert 
# Date of latest revision:     16AUG2023
# Event logging tool Part 3/3

#import library
import logging 

#create my logger obejct
logger =logging.getLogger('my_logger')

#creat handlers (stream and file ) 
terminal_handler + logging.StreamHandler()
file_handler = logging.FileHandler('errors.log')

#set levels for the handlers
terminal_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.ERROR)

#Formatters for log messages
terminal_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')


#pair the formatters with handlers
terminal_handler.setFormatter(terminal_format)
file_handler.setFormatter(file_format)

#add handlers to logger
logger.addHandler(terminal_handler)
logger.addHandler(file_handler)

logger.warning("Warning Message")
logger.error("Error Message")





