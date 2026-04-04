# Print number form 1 to 100.

i = 1
while i<=100 :
    print(i)
    i+= 1

# Print numbers from 100 to 1 
i = 100
while i >= 1 :
    print(i)
    i-= 1

# Print the multiplication table of a number n.

n = int(input("Enter the number : "))
i = 1
while i<= 10 :
    print(n*i)
    i+= 1

# print the elements of a list using while loop.
#my_list = [1, 2, 3, 4, 5]
my_list = [1, 2, 3, 4, 5]   
i = 0
while i < len(my_list) :
    print(my_list[i])
    i+= 1

# Search a number x in this tuple using loop.
# (1,4,9,16,25,36,49,64,81,100) # traverse 
n = int(input("Enter the number : "))
my_tuple = (1,4,9,16,25,36,49,64,81,100)
i = 0
while i < len(my_tuple) :
    if my_tuple[i] == n :
        print("Number found in the tuple.")
    else:
        print("Number not found in the tuple.")
    i+= 1

# Print the element of the following list using loop.
# [1,4,9,16,25,36,49,64,81,100]
list = [1,4,9,16,25,36,49,64,81,100]
for el in list :
    print(el)

# Search for a number x in this tuple using for loop.
tuple = (1,4,9,16,25,36,49,64,81,100)
num = int(input("Enter the number you want "))
for el in tuple:
    if (el == num):
        print("found")
# Range function in for loop
# for i in range (start, stop, step) :
#     statement
# for i in range (10) : # 0 to 9
#     print(i)
# for i in range (1, 11) : # 1 to 10
#     print(i)
# for i in range (1, 11, 2) : # 1 to 10 with step 2
#     print(i)  

sequence = range (1, 11, 2)
for el in sequence :
    print(el)

# WAP to print 1 to 100 using for loop and range.
count = range(101)
for ele in count:
    print(ele)
    