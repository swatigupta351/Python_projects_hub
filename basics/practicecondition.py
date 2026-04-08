# WAP to check if the number is even or odd.
num = int(input("Enter a number :"))
if num % 2 == 0:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")

# WAP to check if the number is positive, negative or zero.
num = int(input("Enter a number :"))
if num > 0:
    print(num, "is a positive number.")
elif num < 0:
    print(num, "is a negative number.")
else:
    print(num, "is zero.")  

# WAP to check if the year is leap year or not.
year = int(input("Enter a year :"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")      

# WAP to find the gratest of 3 numbers entered by the user.

a = int(input("Enter 1st number :"))
b = int(input("Enter 2nd number :"))
c = int(input("Enter 3rd number:"))
if (a >=b and a >= c):
    print(a, " is greatest number")
elif (b >= c):
    print(b, "is greatest number")
else:
    print(c," is greatest number")

# WAP to check if a number is multiple of 7 or not.

mul = int(input("Enter number :"))
if (mul % 7 == 0):
    print(mul, "is multiple of 7")
else:
    print(mul , "is not mltiple of 7")




