# Functions -> Block of statements that perform a specific task.
# def func_name(param1 , param2..): function defination 
  # statements 
# return value 


# function call 
# function_name(arg1,arg2)# function call

# WAF to find average of 3 numbers.
def average(a , b, c): # function defination
    return (a+b+c)/3

print(average(2 , 5, 7)) # function call


# Types of function 
# Builtin function , user defined function 
# Builtin -> print(),len(),range()
# user defined function : user will create according requirements


# WAF to print the length of a list.
def print_len(list):
    print(len(list))
    return(len(list))

cities = ["Delhi", "Agra", "Gudgaon","Kanpur","Lucknow"]
fruits = ["Apple","Banana","Guava","Papaya","watermelon"]
print_len(cities)
print_len(fruits)


# WAF to print the elements of a list in a single line.
def print_elements(list):
    print(*list) # * is used to unpack the list and print the elements in a single line.

print_elements(cities)
print_elements(fruits)

# WAF to find the maximum of 3 numbers.
def max_of_three(a , b , c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
    
print(max_of_three(5 , 10 , 3))

# WAF to find the factorial of a number.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))
print(factorial(0))
print(factorial(1))
print(factorial(10))

# WAF to convert USD to INR.
def usd_to_inr(usd):    
    inr = usd * 82.5
    return inr
print(usd_to_inr(100))

# WAF to find number is even or odd.

def even_odd(n):
    if n % 2 == 0:
        print("even")
    else:
        print("odd")

even_odd(9)
even_odd(10)
even_odd(15)


