import os
import sys

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

""" READ THE FOLDER PATH GIVEN AND RETRIEVE ALL FILES + DIR NAMES. """

try:
    directory_list = os.listdir(directory_path)
    for items in directory_list :
        print(items, end='  ')
    print("")
except OSError as err:
    print("An error occured : \n" + str(err))
    exit()
