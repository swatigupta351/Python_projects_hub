# Local system automation : 
# OS module : basic operation ( python built in module) -> bridge of python who communicate to OS(operating system)
# shutil module : heavy operation 
# sc1-> Created folders and files dynamically
# sc2-> Performed file operations like write and delete
# sc3-> Deleted directories with content 
# linux -> Shell → Linux OS → Folder create(action)
# Python → os module → Linux OS → Folder create (action)
# “os ek module hai jisme already functions defined hote hain, aur hume jis kaam ki need hoti hai us function ko call karte hain.”
import os 
os.system("pwd")

import os 
print(os.getcwd())

## Important* 
# os.system() se command ka output python variable me store nahi hota, isliye subprocess use karte hain”

# subprocess module : it is used to run the command in terminal and get the output in python variable.

# import os
# output = os.system("ls")
# print(output) # it will print the output in terminal but it will return 0 in python variable because os.system() returns the exit status of the command, not the output of the command.

## folder create 
# os.mkdir("demo")

## mutiple folder creation 
# os.makedirs("demo/test/data")

## folder delete 
# os.rmdir("demo")   # empty hona chahiye

# file delete
# os.remove("demo/test/data/file.txt")

## folder delete with content
# os.removedirs("demo/test/data") # it will delete data folder and test folder
# os.removedirs("demo") # it will delete demo folder and all its content

## File rename
# os.rename("demo/test/data/file.txt", "demo/test/data/newfile.txt")

## Listing & Navigation
# os.getcwd()

## Directory change
# os.chdir("demo/test/data")

## Files/folders list
# os.listdir() # list of all files and folders in current directory
# os.listdir("demo") # list of all files and folders in demo directory

## Path Handling
# os.path.join("demo", "test", "data", "file.txt") # it will join all the path and return the complete path
# os.path.exists("demo/test/data/file.txt") # it will return True if file exists
# os.path.isfile("demo/test/data/file.txt") # it will return True if it is a file
# os.path.isdir("demo/test/data") # it will return True if it is a directory

## Linux command run in python
# os.system("ls -l") # it will run the command in terminal and print the output in terminal
# os.system("echo Hello World") # it will print Hello World in terminal        
# os.system("mkdir newfolder") # it will create newfolder in current directory  
# os.system("rm -rf newfolder") # it will delete newfolder in current directory
# os.system("mv demo/test/data/file.txt demo/test/data/newfile.txt") # it will rename file.txt to newfile.txt in demo/test/data directory
# os.system("cp demo/test/data/newfile.txt demo/test/data/copyfile.txt") # it will copy newfile.txt to copyfile.txt in demo/test/data directory
# os.system("cat demo/test/data/newfile.txt") # it will print the content of newfile.txt in terminal
# os.system("ls -l demo/test/data") # it will list all files in demo/test/data directory with details




