str = "This is Swati"
str1 = 'This is swati'
str2 = ''' This is swati'''
# Escape sequence characters -> \n , \t , \', \" , \\ 
str3 = "This is swati \"gupta\""
str4 = 'This is swati \'gupta\''
str5 = "This is swati \n gupta" # new line
str6 = "This is swati \t gupta" # tab space
print(str)
print(str1)
print(str2)
print(str3)
print(str4)
print(str5)
print(str6) 

# Basic string operations
str7 = "Hello"
str8 = "World"
print(str7 + " " + str8) # concatenation
print(str7 * 3) # repetition
print(len(str7)) # length of string
print(str7[0]) # indexing
print(str7[1:4]) # slicing 1 to 3 index tak print karega
print(str7[-1]) # last character
print(str7[:3]) # print from start to index 2
print(str7[2:]) # print from index 2 to end
print(str7[::2]) # print every 2nd character
print(str7[::-1]) # print string in reverse
print(str7[1:5:2]) # print from index 1 to 4 with step 2
print(str7[1:5:3]) # print from index 1 to 4 with step 3
print(str7[1:len(str7)]) # print from index 1 to end
print(str7.lower()) # convert to lowercase
print(str7.upper()) # convert to uppercase
print(str7.replace("l", "x")) # replace characters
print(str7.split("e")) # split string
print(str7.strip()) # remove whitespace from both ends
# main string m change nahi hoga , new string banega.
# string is immutable -> we cannot change the string after it is created.

