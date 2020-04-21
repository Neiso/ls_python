import os
import sys
from function import *

def ls():
    """basic ls function. Check the README.md for more information."""
    

    """ 
        READ THE ARGV FROM CONSOLE INPUT.
        4 cases:
            - 'ls.py /path/to/dir'
            - 'ls.py'
            - 'ls.py -l /path/to/dir' in this specific order
            - 'ls.py -l'
        else it raises an error.
        Each cases call the function get_dir_items which return all the files 
        or directory found with the matching prefix. If nothing has been found,
        it returns nothing.
    """
    try :    
        if len(sys.argv) == 2 and sys.argv[1] != "-l":
            directory_path = sys.argv[1]
            directory_items, directory_path = get_dir_items(directory_path)
            for items in directory_items :
                print(items, end='  ')
            if (len(directory_items) >= 1):
                print("")
        elif len(sys.argv) == 3:
            if(sys.argv[1] != "-l"):
                raise ValueError("Option " + sys.argv[1] + " not handled yet.")
            directory_path = sys.argv[2]
            ls_list(directory_path)
        elif len(sys.argv) == 2 and sys.argv[1] == "-l":
            directory_path = os.getcwd()
            ls_list(directory_path)
        elif len(sys.argv) == 1:
            directory_path = os.getcwd()
            directory_items, directory_path = get_dir_items(directory_path)
            for items in directory_items :
                print(items, end='  ')
            if (len(directory_items) >= 1):
                print("")
        else :
            raise ValueError("Too many arguments given.")
    except ValueError as err :
        print("An error occured while reading user's input : \n\t" + str(err))
        return 0
    
    

if __name__ == "__main__":
    ls()