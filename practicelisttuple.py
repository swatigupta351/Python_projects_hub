# WAP to ask the user to enter 5 movies and store them in a list  and print the list.
movies = []
for i in range(5):
    movie = input("Enter the name of a movie: ")
    movies.append(movie)
print("The movies you entered are:")
print(movies)

# WAP to ask the user to enter 5 movies and store them in a tuple and print the tuple.
movies_tuple = ()
for i in range(5):
    movie = input("Enter the name of a movie: ")
    movies_tuple += (movie,)
print("The movies you entered are:")
print(movies_tuple) 

# WAP to check the list is palindrome or not.
# [1,2,3,2,1]
list = [1, 2, 3, 2, 1]
list_copy = list.copy()
list_copy.reverse()
if list == list_copy:
    print("The list is a palindrome.")
else:    print("The list is not a palindrome.")     

# WAP to count number of students with the "A" grade in a list of grades.
grades = ['A', 'B', 'A', 'C', 'A', 'B', 'A']
count_A = grades.count('A')
print("The number of students with 'A' grade is:", count_A)

