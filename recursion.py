# Recursion -> When a function calls itself repeatedly.

# Recursive function 
def show(n):
    if (n == 0): # Basecase -> decides when recursion will stop
        return
    print(n)
    show(n-1)


show(7)
show(10)

# Write a recursive function to print all elements in a list.
def print_elements(idx, list):
    if (idx == len(list)):
        return
    print(list[idx])
    print_elements(idx+1 , list)

name = ["swati", "Anita" , "Sanchit", "Umang"]
print_elements(0 , name)

# Write a recursive function to find the sum of first n natural numbers.
def sum_natural(n):
    if n == 0:
        return 0
    else:
        return n + sum_natural(n-1)
    
print(sum_natural(5))
