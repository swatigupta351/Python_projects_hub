# break -> Used to terminate the loop when encountered.
# continue -> Terminates execution in the current iteration and continue    execution of the loop with the next iteration.

i = 1
while i <= 10 :
    print(i)
    if i == 4 :
        break
    i+= 1

i = 1
while i <= 10 :
    if i == 4 :
        i+= 1
        continue
    print(i)
    i+= 1   

# for loops are used for sequencial transverse. For travilling list , tuple, string.

# Use for loop → when the number of iterations is known.
# Use while loop → when the number of iterations is not known.

# for el in my_list :
#     print(el)

nums = [1, 2, 3, 4, 5]
for num in nums :
    print(num)
    if num == 3 :
        break


str = "Hello World"
for ch in str :
    if ch == 'o' :
        continue
    print(ch)


    
