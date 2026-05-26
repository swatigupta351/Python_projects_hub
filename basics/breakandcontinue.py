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
    


    
