#1/usr/bin/python3

# Script Name:                 401-ops-class0.py               
# Class Name:                  Ops 401d8
# Author Name:                 David Siebert 
# Date of latest revision:     18JUL2023
# In Python create a script that utilizes OS.WALK to crawl the tree hierarchy.

#import libraries 
import os 

# begin to recurisvely crawl directory 
for root, dirs, files in os.walk(".", topdown=True):
# up one level
#for root, dirs, files in os.walk("../", topdown=True):  
  # hits, concatenate the current directory path to the left of the result
  for file in files:
      print(os.path.join(root,file))
  for dir in dirs:
      print(os.path.join(root,dir))
      
