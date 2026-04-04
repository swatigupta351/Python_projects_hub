# Built in data types list and tuple 
# list -> mutable , different data types together
# tuple -> immutable , same type of data types
list = [4,5,89,23,"apple","swati",67.5]
print(list)
print(type(list))
print(len(list))
# indexing and slicing 
print(list[3])
print(list[0:4])
print(list[:4])
print(list[2:])
print(list[1:4:2]) # 1 to 4 by step 2
list[0] = "sanchit"
print(list)
tuple = (4,5,89,23,"apple","swati",67.5)
print(tuple)
print(type(tuple))
print(len(tuple))
# indexing and slicing
print(tuple[3])
print(tuple[0:4])
print(tuple[:4])
print(tuple[2:])
print(tuple[1:4:2]) # 1 to 4 by step 2
# tuple[0] = "sanchit" # error because tuple is immutable   
tup = () # empty tuple 
tup = (1,) # (1) it is not allowed , for single value comma is mandatory to create tuple 
tup = ("Hello")
tup = (2.5,)
# tuple methods
print(tuple.count(5)) # count the number of times 5 is present in tuple
print(tuple.index("apple")) # return the index of first occurrence of "apple" in tuple
