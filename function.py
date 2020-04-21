import os
import stat
from pwd import getpwuid
import datetime

def find_prefix(dir_path):
    dirs = dir_path.split("/")
    boolean = False
    if len(dirs) == 2:
        parent_dir = "/"
        child = dirs[-1]
    else :
        parent_dir = ""
        for i in dirs[:-1]:
            parent_dir += (str(i) + "/")
        child = dirs[-1]
    try:
        directory_list = os.listdir(parent_dir)
        for items in directory_list :
            if items.startswith(child):
                print(items, end="  ")
                boolean = True
        if boolean:
            print()
        else :
            print("No file or directory found matching prefix.")
        return (1)
    except OSError as err:
        return (0)


def get_dir_items(directory_path):
    """ 
        READ THE FOLDER PATH GIVEN AND RETRIEVES ALL FILES + DIR NAMES. 
        IF THE DIRECTORY IS NOT FIND, IT RAISES AN OSError WHICH LEADS TO
        A SEARCH FOR PREFIX.    
    """
    try:
        directory_list = os.listdir(directory_path)
        return directory_list
    except OSError as err:
        if(not find_prefix(directory_path)):
            print("An error occured while checking for the directory: \n\t" + str(err))
        exit()

def ls_list(directory_path):
    if (directory_path[-1] != "/"):
        directory_path += "/"
    items = get_dir_items(directory_path)
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
    link_size = 0
    id_size = 0
    group_size = 0
    size_size = 0
    date_size = 0
    for item in items_desc:
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
    for item in items_desc:
        output = ""
        output += item[0]
        output += (" " * (link_size - len(item[1]) + 1)) + item[1]
        output += (" " * (id_size - len(item[2]) + 1)) + item[2]
        output += (" " * (group_size - len(item[3]) + 1)) + item[3]
        output += (" " * (size_size - len(item[4]) + 1)) + item[4]
        output += (" " * (date_size - len(item[5]) + 1)) + item[5]
        output += " " + item[6]
        print(output)