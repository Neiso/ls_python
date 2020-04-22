import os
import stat
from pwd import getpwuid
import datetime
from operator import itemgetter

def find_prefix(dir_path):
    """Split the given path to get parent path and child prefix."""
    dirs = dir_path.split("/")
    boolean = False
    if len(dirs) == 2:
        if dir_path[0:2] == "./":
            parent_dir = os.getcwd()
        else :
            parent_dir = "/"
        child = dirs[-1]
    else :
        parent_dir = ""
        for i in dirs[:-1]:
            parent_dir += (str(i) + "/")
        child = dirs[-1]
    try:
        directory_list = os.listdir(parent_dir)
        return directory_list, child, parent_dir
    except OSError as err:
        print(err)
        exit()


def get_dir_items(directory_path):
    """ 
        Read the folder path given and retrieves all files + dir names. 
        If the directory is not find, it raises an oserror which leads to
        a search for prefix. If the prefix didn't match, it simply display the
        error and exit. If the prefix did match, it returns a list of items containing
        all the matching items.
    """
    try:
        directory_list = os.listdir(directory_path)
        return directory_list, directory_path
    except OSError as err:
        directory_list, child, directory_path = find_prefix(directory_path)
        if(not directory_list):
            print("An error occured while checking for the directory: \n\t" + str(err))
            exit()
        else :
            return_list = []
            for items in directory_list :
                if items.startswith(child):
                    return_list.append(items)
            if len(return_list) >= 1:
                return return_list, directory_path
            else :
                print("No matching found with the prefix.")
                exit()

def ls_list(directory_path):
    """
        Get all information from files using os.stat module.
        Then display it properly with correct amount of space in between
        parts and in alphabetical order.
    """
    items, directory_path = get_dir_items(directory_path)
    if (directory_path[-1] != "/"):
        directory_path += "/"
    items_desc = []
    for item in items:
        item_desc = []
        mode = os.stat(directory_path + item).st_mode
        symbolic_index = os.stat(directory_path + item)
        item_desc.append(stat.filemode(mode))
        item_desc.append(str(symbolic_index[3]))
        item_desc.append(getpwuid(symbolic_index[4]).pw_name)
        item_desc.append(getpwuid(symbolic_index[5]).pw_name)
        item_desc.append(str(symbolic_index[6]))
        timestamp = symbolic_index[9]
        date = datetime.datetime.fromtimestamp(timestamp)
        item_desc.append(f"{date:%Y-%m-%d %H:%M}")    
        item_desc.append(item)
        items_desc.append(item_desc)
    items_desc = sorted(items_desc, key=lambda x: x[6].lower())
    return(items_desc)

def display_items(items, l_arg):
    if not l_arg:
        for item in items :
            print(item, end='  ')
        if (len(items) >= 1):
            print("")
    elif l_arg:
        link_size = 0
        id_size = 0
        group_size = 0
        size_size = 0
        date_size = 0
        for item in items:
            if len(item[1]) > link_size:
                link_size = len(item[1])
            if len(item[2]) > id_size:
                id_size = len(item[2])
            if len(item[3]) > group_size:
                group_size = len(item[3])
            if len(item[4]) > size_size:
                size_size = len(item[4])
            if len(item[5]) > date_size:
                date_size = len(item[5])
        for item in items:
            output = ""
            output += item[0]
            output += (" " * (link_size - len(item[1]) + 1)) + item[1]
            output += (" " * (id_size - len(item[2]) + 1)) + item[2]
            output += (" " * (group_size - len(item[3]) + 1)) + item[3]
            output += (" " * (size_size - len(item[4]) + 1)) + item[4]
            output += (" " * (date_size - len(item[5]) + 1)) + item[5]
            output += " " + item[6]
            print(output)

