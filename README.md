# ls_python
A simple version of ls coded in python

v0.1 features:
  - lists all files of a specified folder.
  - lists all files beginning with a given prefix.
  - has an option "-l" to display the mode and the creation date of the files.
  
Exemples :
  - ls.py /path/to/folder/ <br>
      some_file <br>
      another_file <br>

  - ls.py /path/to/folder/som<br>
    some_file<br>

  -  ls.py -l /path/to/folder<br>
    rwxr--r-- 2017-12-15 17:44 some_file<br>
    rwxr-xr-x 2017-12-15 17:44 another_file<br>
