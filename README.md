# DS5111_FALL2023_SW2_Lab

To get the make command to work, I had to install make by typing sudo apt install make.

To make the python3 -m venv env, I had to run sudo apt update and then sudo apt install python3.10-venv. This package wasn’t previously installed.  I wouldn’t have known this without the error message. 

In a makefile, each line is its own bash call. Even though the previous line creates the virtual environment, in order for it to be activated and for the packages to be put into that environment, the activation call needs to be on the same line as the pip install.

The job run would not execute if there were a file called run, but to fix this, we could add a line: .PHONY: run before defining the run target, and that would tell the program that the label “run” doesn’t refer to a folder.

Sys.path is a list of directories where python is looking for things. By appending “.” - the current directory - to this path, you’re adding the current directory to the list of locations to find whatever file or package is being searched for. In this case, Python will be looking for the clockdeco_param.py script, so it can look in any of the directories that are part of the path, including the current one.

Extra Credit

To print the tree structure without the env directory, I used the line: tree -I env.

The meaning of asterisks is to exclude any file ending with __pycache__ that is in any directory, and with any text preceding the __pycache__. The asterisks are  acting like a wildcard to find any pycache files in any directory or subdirectory.

I included versions for pytest and pylint in my requirements.txt file.

The construct if __name__ ==”__main__” is checking to see if a script is being run as the main program, or if it has been imported into another script as a module. When a script is run, the __name__ is assigned to “main” if it’s the main script, and if it’s a module, the __name__ will be assigned to the name of that script instead. (So, if we’re importing a python file called “test.py” as a module into another script, then __name__ will be “test”, whereas if we run test.py on its own, __name__ will be “main”. If the condition is met - that is, the script is being run on its own and not imported - then the action below that if statement will be executed. If not, then the action won’t be executed.

If you add two print statements, one before if __name__ ==”__main__” and one after, the statement before will always print out, whether or not the file is called directly or imported into another script. However, the print statement below (indented under the if statement) will only print out if the file is called directly, and will not print out if it’s imported as a module.
