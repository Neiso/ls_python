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
        else it raises an error and display it properly.
        Each cases call the function get_dir_items which return all the files 
        or directory found with the matching prefix. If nothing has been found,
        it returns nothing.
        When every items are gathered, they are being displayed in console afterwards in the display
        function.
    """
    l_arg = False
    try :    
        if len(sys.argv) == 2 and sys.argv[1] != "-l":
            directory_path = sys.argv[1]
            directory_items, directory_path = get_dir_items(directory_path)
        elif len(sys.argv) == 3:
            if (sys.argv[1][0] != "-"):
                raise ValueError("Too many arguments given or wrong order.")
            elif(sys.argv[1] != "-l"):
                raise ValueError("Option " + sys.argv[1] + " not handled yet.")
            l_arg = True
            directory_path = sys.argv[2]
            directory_items = ls_list(directory_path)
        elif len(sys.argv) == 2 and sys.argv[1] == "-l":
            l_arg = True
            directory_path = os.getcwd()
            directory_items = ls_list(directory_path)
        elif len(sys.argv) == 1:
            directory_path = os.getcwd()
            directory_items, directory_path = get_dir_items(directory_path)
        else :
            raise ValueError("Too many arguments given.")
    except ValueError as err :
        print("An error occured while reading user's input : \n\t" + str(err))
        return 0

    if not l_arg:
        directory_items = sorted(directory_items, key=lambda x: x.lower())
    display_items(directory_items, l_arg)
    return (directory_items)
    
    

if __name__ == "__main__":
    ls()