import os
import sys
from function import *

""" READ THE ARGV FROM CONSOLE INPUT"""

try :    
    if len(sys.argv) == 2:
        directory_path = sys.argv[1]
    elif len(sys.argv) == 3:
        directory_path = sys.argv[2]
    elif len(sys.argv) == 1:
        directory_path = os.getcwd()
    else :
        raise ValueError("Too many arguments given.")
except ValueError as err :
    print("An error occured : \n" + str(err))
    exit()

""" 
    READ THE FOLDER PATH GIVEN AND RETRIEVES ALL FILES + DIR NAMES. 
    IF THE DIRECTORY IS NOT FIND, IT RAISES AN OSError WHICH LEADS TO
    A SEARCH FOR PREFIX.    
"""


try:
    directory_list = os.listdir(directory_path)
    for items in directory_list :
        print(items, end='  ')
    print("")
except OSError as err:
    if(not find_prefix(directory_path)):
        print("An error occured : \n" + str(err))
    exit()
