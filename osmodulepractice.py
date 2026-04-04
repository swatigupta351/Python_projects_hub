# WAP to create a file with in folder A . and move this file to folder B. 
import os
print("currrent Directory:", os.getcwd())
folder_name = "testing"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(folder_name, "folder created")
else:
    print(folder_name , "folder already exist")
os.chdir(folder_name)
print("now working in:" , folder_name)
# create subfolders
folders = ["logs", "data", "scripts"]
for folder in folders:
    if not os.path.exists(folder):
        os.mkdir(folder)
        print(folder , "created")
    else: 
        print(folder, "already exist")
#Create a file inside logs
log_file_path = os.path.join("logs" , "app.log")
with open(log_file_path , "w") as f:
    f.write("File is created\n")
print("file is created at" , log_file_path)

# create all files and folders
print("structure" , os.listdir())


os.system("dir")



