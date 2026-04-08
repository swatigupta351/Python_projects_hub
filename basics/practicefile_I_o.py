# Create a new file "practice.txt" using python. Add the following data in it.
# Hi everyone, 
# We are learning python file I/O.
# I like python prgraming.

f = open("practice.txt", "w+")
f.write('''Hi everyone,
We are learning python file I/O.
I like python prgraming.''')
f.close()

# WAF that replace all occurance of python with java in above file.
with open("practice.txt" , "r") as f:
    data = f.read()
new_data = data.replace("python" , "Java")
print(new_data)

with open("practice.txt" , "w") as f:
    data = f.write(new_data)

# Search if the word learning word is exit or not in the file.
with open("practice.txt" , "r")as f:
    data = f.read()
    if (data.find("learning") != -1):
        print("found")
    else:
        print("not found")


