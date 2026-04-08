# # # Numpy : ye numeric data ke liye high-performance tool hai

# # # List : each element is a object and has seperate memory , manually loop required 
# # # numpy : continous memory location , optimized memory , automatic loop 

# # # example for list : 

# # # # a = [1, 2, 3]
# # # # b = [4 ,5, 6]
# # # # c = []
# # # # i = 0
# # # # for i in range(len(a)):
# # # #     c.append(a[i] + b[i])
# # # # print(c)

# # # # # using numpy 

# # # # import numpy as np 
# # # # a = np.array([1,2,3])
# # # # b = np.array([4,5,6])

# # # # c = a + b
# # # # print(c)



# # import numpy as np

# # # # a = np.array([1,2,3,4,5,6,7,8,9,10])
# # # # print(a)

# # # # PART 1: Array Creation
# # # from time import sleep

# import numpy as np 
# # # b = np.array([1,2,3,4,5])
# # # print(b)
# # # a = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# # # print(a) # show 2D array 
# # # zero = np.zeros((3,4)) # np.zeros(row,cloumn) create array valued 0. 
# # # print(zero)
# # # one = np.ones((2,3)) # np.ones(row,column) create array valued 1. 
# # # print(one)
# # # range = np.arange(1,10,2) # np.arrange(start,stop,step)
# # # print(range)
# # # linspc = np.linspace(0,1,4) # equal intervals me numbers deta hai (start , stop , step)
# # # print(linspc)
# # # empt = np.empty((2,2)) # show any garbage value 
# # # print(empt)


# # # # PART 2: Shape & Structure

# # # c = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# # # print(c.shape) # array shape like  (row , cloumn)
# # # print(c.ndim) # array dimention like 1D,2D , 3D 
# # # print(c.size)# total elements count 
# # # d = np.array([1,2,3,4,5,6,7,28,9,10]) 
# # # print(d.reshape(2,5)) # for reshape the data according (row , column ) our requirement, total elements must be same.
# # # print(c.flatten()) # convert to 1D


# # # PART 3: Math Operations & Vectorization

# # e = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# # f = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# # # 1. Basic Arithmetic (element-wise)
# # print(e + f)
# # print(e - f)
# # print(e * f)
# # print(e / f)
# # print(e % f)
# # print(e ** f)

# # # 2. Power & Square
# # print(e ** 2)
# # sqr = np.square(e)
# # print(sqr)
# # # 3. Square Root
# # sqrroot = np.sqrt(e)
# # print(sqrroot)

# # # 4. Aggregate Functions
# # print(np.sum(e))
# # print(np.mean(e))
# # print(np.min(e))
# # print(np.max(e))

# # # 5. Standard Deviation
# # print(np.std(e))

# # 6. Vectorization (loop ke bina pura array process)

# # without numpy 
# c = []
# i = 0
# e = [1,2,3,4,5]
# for i in range(len(e)):
#     c.append((e[i] * 2))
# print(c)

# with numpy, loop not required 
# fast and clean without using loop operation on each element 
import numpy as np
noloop = np.array([1,2,3,4,5])
c = [noloop * 2]
print(c)

# 7. Comparison Operations
print(noloop > 2)

# 8. Filtering
print(noloop[noloop > 2]) # print number greater than 2 

# PART 4: Indexing & Slicing
# 1. 1D Array Indexing

import numpy as np
a = np.array([1,2,3,4,5])
print(a[0]) # value on index 0 
print(a[3]) # value  on index 3

# 2. Negative Indexing
print(a[-2]) # value in index -2 

# 3. Slicing (range nikalna)
print(a[1:3]) # index 1 to 2 ( start : end )(end is not included)

# 4. Step slicing
print(a[0:4:2]) # (start:stop:step)

# 2D Array Indexing
b = np.array([[1,2,3],
              [4,5,6]])
print(b[0,1]) # 0 row , 1 column 
print(b[1,2]) # 1 row , 2 column
print(b[0]) # row access 
print(b[:,1]) # column access : sub rows , column index ,1

# 8. Sub-matrix
print(b[0:2, 1:3])


# PART 5: Random & Utility
# 1. Random Numbers
import numpy as np

print(np.random.rand(3)) # har bar output different 
print(np.random.randint(1, 10, 5)) # random integers 
a = np.array([1,2,3,4])

# 2. Shuffle & Permutation
np.random.shuffle(a) # numbers suffle ho jayege 
print(a)

# 3. Sorting
a = np.array([3,1,2])

print(np.sort(a))

# 4. Where (search)
a = np.array([10,20,30,20])

print(np.where(a == 20))

# 5. Unique values
print(np.unique([1,2,2,3,3,4]))

# 6. Clip (range limit)
a = np.array([5,10,15,20])

print(np.clip(a, 10, 15))

# 7. Concatenate (join arrays)
a = np.array([1,2])
b = np.array([3,4])

print(np.concatenate((a,b)))

# 8. Stack (2D join)
print(np.vstack((a,b)))
print(np.hstack((a,b)))
