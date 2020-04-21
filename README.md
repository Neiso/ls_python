# ls_python
A simple version of ls coded in python

v0.1 features:
  - lists all files of a specified folder.
  - lists all files beginning with a given prefix.
  - has an option "-l" to display the mode and the creation date of the files.
  
Exemples :
  - ls.py /path/to/folder/ :
      some_file
      another_file

  - ls.py /path/to/folder/som
    some_file

  -  ls.py -l /path/to/folder
    rwxr--r-- 2017-12-15 17:44 some_file
    rwxr-xr-x 2017-12-15 17:44 another_file
