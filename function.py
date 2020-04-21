import os

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
            print("No file/directory found.")
        return (1)
    except OSError as err:
        return (0)