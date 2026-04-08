# WAP to input user's name and print its length.
name = input("Enter your name :")
print("Length of your name is :", len(name))

# WAP to input user's name and print it in reverse order.
name = input("Enter your name :")
print("Your name in reverse order is :", name[::-1])

#WAP to find the occurrence of a character in a string.
str = input("Enter a string :")
char = input("Enter a character to find its occurrence :")
count = str.count(char)
print("The occurrence of character", char, "in the string is :", count)
