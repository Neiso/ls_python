import unittest
import subprocess

class Testls(unittest.TestCase):
    def test_simple(self):
        """ Simple test with full correct path with no -l option"""

        output = subprocess.check_output("python3 ls.py", shell=True)
        expected = ".git  __pycache__  function.py  ls.py  README.md  test.py  tests  \n"  
        output2 = subprocess.check_output("python3 ls.py ./tests", shell=True) 
        expected2 = "path  \n"     
        output3 = subprocess.check_output("python3 ls.py ./tests/path/to", shell=True)      
        expected3 = "acces.log  another_dir  error.log  folder  Hello.txt  some_dir  World.txt  \n"
        self.assertEqual(output.decode("utf-8"), expected)
        self.assertEqual(output2.decode("utf-8"), expected2)
        self.assertEqual(output3.decode("utf-8"), expected3)

    def test_simple_prefix(self):
        """Simple test with prefix and no -l option"""

        output = subprocess.check_output("python3 ls.py ./t", shell=True)
        expected = "test.py  tests  \n"
        output2 = subprocess.check_output("python3 ls.py ./tests/path/t", shell=True)
        expected2 = "to  traffic.log  \n"
        output3 = subprocess.check_output("python3 ls.py ./tests/path/to/folder/s", shell=True)
        expected3 = "some_file  \n"
        output4 = subprocess.check_output("python3 ls.py ./tests/path/to/a", shell=True)
        expected4 = "acces.log  another_dir  \n"
        output5 = subprocess.check_output("python3 ls.py ./tests/path/to/error.log", shell=True)
        expected5 = "error.log  \n"

        self.assertEqual(output.decode("utf-8"), expected)
        self.assertEqual(output2.decode("utf-8"), expected2)
        self.assertEqual(output3.decode("utf-8"), expected3)
        self.assertEqual(output4.decode("utf-8"), expected4)
        self.assertEqual(output5.decode("utf-8"), expected5)

    def test_long_list_enabled(self):
        """
            Simple test with -l option enabled. 
            Pay attention that if you modify any files, this test might
            be wrong since the last modification date will change.
        """
        self.maxDiff = None
        output = subprocess.check_output("python3 ls.py -l", shell=True)
        expected = "drwxr-xr-x 8 djulian djulian 4096 2020-04-22 12:18 .git\ndrwxr-xr-x 2 djulian djulian 4096 2020-04-22 12:16 __pycache__\n-rw-r--r-- 1 djulian djulian 4135 2020-04-22 12:15 function.py\n-rwxr-xr-x 1 djulian djulian 2045 2020-04-22 12:14 ls.py\n-rw-r--r-- 1 djulian djulian  512 2020-04-21 12:33 README.md\n-rwxr-xr-x 1 djulian djulian 5703 2020-04-22 12:20 test.py\ndrwxr-xr-x 4 djulian djulian 4096 2020-04-22 10:49 tests\n"
        output2 = subprocess.check_output("python3 ls.py -l ./tests", shell=True)
        expected2 = "drwxr-xr-x 3 djulian djulian 4096 2020-04-22 12:28 path\ndrwxr-xr-x 2 djulian djulian 4096 2020-04-22 10:49 test3\n"
        output3 = subprocess.check_output("python3 ls.py -l ./tests/path/to/folder/", shell=True)
        expected3 = "-rwxr-xr-x 1 djulian djulian 0 2020-04-22 10:48 another_file\n-rwxr--r-- 1 djulian djulian 0 2020-04-22 10:48 some_file\n"        
        output4 = subprocess.check_output("python3 ls.py -l ./tests/path/t", shell=True)
        expected4 = "drwxr-xr-x 5 djulian djulian 4096 2020-04-22 10:57 to\n-rw-r--r-- 1 djulian djulian    0 2020-04-22 10:51 traffic.log\n"
        output5 = subprocess.check_output("python3 ls.py -l ./tests/path/to", shell=True)
        expected5 = "-rw-r--r-- 1 djulian djulian    0 2020-04-22 10:49 acces.log\ndrwxr-xr-x 2 djulian djulian 4096 2020-04-22 10:48 another_dir\n-rw-r--r-- 1 djulian djulian    0 2020-04-22 10:49 error.log\ndrwxr-xr-x 2 djulian djulian 4096 2020-04-22 10:57 folder\n-rw-r--r-- 1 djulian djulian    0 2020-04-22 10:48 Hello.txt\ndrwxr-xr-x 2 djulian djulian 4096 2020-04-22 10:57 some_dir\n-rw-r--r-- 1 djulian djulian    0 2020-04-22 10:48 World.txt\n"
        # self.assertEqual(output.decode("utf-8"), expected)
        self.assertEqual(output2.decode("utf-8"), expected2)
        self.assertEqual(output3.decode("utf-8"), expected3)
        self.assertEqual(output4.decode("utf-8"), expected4)
        self.assertEqual(output5.decode("utf-8"), expected5)

    def test_error(self):
        """The program shouldn't exit unexpectedly."""

        output = subprocess.check_output("python3 ls.py ./yh", shell=True)
        expected = "No matching found with the prefix.\n"  
        output2 = subprocess.check_output("python3 ls.py ./TESTS", shell=True)
        expected2 = "No matching found with the prefix.\n"
        output3 = subprocess.check_output("python3 ls.py ./TESTS -l", shell=True)
        expected3 = "An error occured while reading user's input : \n\tToo many arguments given or wrong order.\n"
        output4 = subprocess.check_output("python3 ls.py -g", shell=True)
        expected4 = "[Errno 2] No such file or directory: ''\n"
        output5 = subprocess.check_output("python3 ls.py -l ./tests test.py", shell=True)
        expected5 = "An error occured while reading user's input : \n\tToo many arguments given.\n"
        output6 = subprocess.check_output("python3 ls.py ./tests test.py", shell=True)
        expected6 = "An error occured while reading user's input : \n\tToo many arguments given or wrong order.\n"
        self.assertEqual(output.decode("utf-8"), expected)
        self.assertEqual(output2.decode("utf-8"), expected2)
        self.assertEqual(output3.decode("utf-8"), expected3)
        self.assertEqual(output4.decode("utf-8"), expected4)
        self.assertEqual(output5.decode("utf-8"), expected5)
        self.assertEqual(output6.decode("utf-8"), expected6)

if __name__ == '__main__':
    unittest.main()