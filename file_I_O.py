# Python can be used to perform operations on a file. ( read and write data)
# Types of all data 
# 1 -> Text files -> txt,docs,logs
# 2 -> Binary files -> mp4, png , jpeg ...

# f = open("path to file","mode") -> open a file in a specific mode
# mode -> "r" -> read mode (default) , "w" -> write mode , "a" -> append mode
# f.close() -> close the file

f = open("test.txt" , "r")
# data = f.read()
# data = f.read(5) # entire data at a time
data = f.readline() # read oneline at a time.
print(data)
print(type(data))
f.close()


# Write data in file.
f = open("test.txt" , "w") # overwrite 
f.write("Hi ,I am swati gupta ")
f.close()

f = open("test.txt" , "a") # append
f.write("Hi ,I am swati gupta ")
f.close()

# write mode will create new file.
f = open("demo.txt" , "w") # overwrite 
f.write("Hi ,I am swati gupta ")
f.close()

# with Syntax 
with open("demo.txt" , "r") as f: 
    print(f.read())

# to delete file 
import os 
os.remove("demo.txt")
