# Store following word meaning in python dictionary.
# table : " a piece of furniture" , "list of facts and figures"
# cat : "a small animal"
# word_meaning = {
#     "table" : ["a piece of furniture", "list of facts and figures"],
#     "cat" : "a small animal"
# }
# print(word_meaning)
# print(word_meaning["table"]) # Accessing value using key
# word_meaning["cat"] = "a domestic animal" # Modifying value using key
# print(word_meaning)
# word_meaning["dog"] = "a domestic animal" # Adding new key-value pair
# print(word_meaning)
# del word_meaning["dog"] # Deleting key-value pair
# print(word_meaning)

# # you are given a list of subjects for students. Assume one classroom is required for 1 subject.how many classroom are needed by all students.
# subjects = {"python","java","c++","python","javascript","java","python","java","c++","c"}
# classroom = (len(subjects))
# print(classroom, " are needed")

# WAP to enter marks of 3 subjects from the user and store them in a dictionary.start with an empty dictionary and add one by one. Use subject name as key and marks as value.

dic = {}
x = int(input("Enter Physics marks :"))
dic.update({"phy":x})
x = int(input("Enter Maths marks:"))
dic.update({"Maths":x})
subjects = int(input("Enter chemistry marks :"))
dic.update({"chem":x})
print(dic)

