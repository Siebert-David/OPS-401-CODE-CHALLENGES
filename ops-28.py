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
file_handler = logging.FileHandler(filename)
