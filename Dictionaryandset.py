# Dictionary are used to store data in key-value pairs. It is a collection which is ordered, changeable and does not allow duplicates.
# WAP to create a dictionary of 5 students with their names and ages and print the dictionary.
students = {
    "Alice": 20,
    "Bob": 22,
    "Charlie": 19,
    "David": 21,
    "Eve": 20
}
print("The students and their ages are:")
print(students)
print(type(students))
print(students["Alice"]) # Accessing value using key
students["Alice"] = 21 # Modifying value using key
print(students)
students["Frank"] = 23 # Adding new key-value pair
print(students)
del students["Frank"] # Deleting key-value pair
print(students) 

# Nested Dictionary 
student = {
    "name" : "Swati Gupta",
    "rollno" : 46687,
    "subjects" :{
        "physics" : 97,
        "chemistry" : 93,
        "maths" : 95,
        "Hindi" : 80,
        "English" : 85,
    }
}
print(student)

# empty dictionary
empty_dict = {}

# set is the collection of the unordered items.
# each element in the set must be unique and immutable.
# it ignores to print duplicate items. and it is not count duplicate items.
# set is mutable itself but the elements of the set must be immutable.

collection = {1,2,3,3,4,4,4,"Hello", "world",5.7,9.8}
print(collection)
print(type(collection))
print(len(collection))

# empty set
empty_set = set()

# create set for union and intersection.

set1 = {1,2,3,2,4,4,1,6,7}
set2 = {4,5,2,6,1,2,7,4}
print(set1.union(set2)) # combine both sets value remove duplicates
print(set1.intersection(set2)) # common in both sets 


