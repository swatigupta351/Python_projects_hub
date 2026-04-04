# os.system() → sirf command run
# 👉 subprocess → command run + output control

# subprocess module = Python ka module jo system commands run karta hai (better than os.system)
# import subprocess

# result = subprocess.run(["command"], capture_output=True, text=True)
# print(result.stdout) Ye actual output hai (jo terminal me dikhta)
# print(result.stderr) # Agar error aaya to yaha dikhega
# print(result.returncode) # status code -> 0 = success , non zero = error 

# example : run command 
import subprocess 
result = subprocess.run(["pwd"], capture_output=True, text=True)
print("output" , result.stdout)
print("Error:", result.stderr)
print("status :", result.returncode)

# Example run multiple commands 
commands = ["pwd", "ls", "whoami"]
for cmd in commands:
    result = subprocess.run([cmd], capture_output= True, text= True)
    print(cmd, "output: " , result.stdout)

import subprocess
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(result.stdout)

# WAP file exists or not in this folder.

import subprocess
result = subprocess.run(["ls"], capture_output=True, text=True)
if "test.txt" in result.stdout:
    print("file exist")
else:
    print("file not exist")




