#!/usr/bin/python3

# Script Name:                 401-ops-class07.py               
# Class Name:                  Ops 401d8
# Author Name:                 David Siebert 
# Date of latest revision:     19JUL2023
# In Python create a script that utilizes OS.WALK to crawl the tree hierarchy. Recursively encrypt a single folder and all its contents. Recursively decrypt a single folder that was encrypted by this tool.

#root: Prints out directories only from what you specified
#dirs: Prints out sub-directories from root
#files: Prints out all files from root and directories

#import libraries 
import os 

# begin to recurisevly crawl directory topdown=false == bottom to top. topdown=True == top to bottom
for root, dirs, files in os.walk(".", topdown=True):
# up directory one level (below)
#for root, dirs, files in os.walk("../", topdown=True):  
  # hits, concatenates the current directory path to the left of the result
  for file in files:
      print(os.path.join(root,file))
  for dir in dirs:
      print(os.path.join(root,dir))
      
...