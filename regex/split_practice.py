# text = "Hello World ! See you soon"
# print(text.split())

# # default seperator space 
# # ['Hello', 'World', '!', 'See', 'you', 'soon']
# print(text.split("!"))
# #['Hello World ', ' See you soon']


# text = "mera naam raj hai"
# result = text.split()

# print(result)     # ['mera', 'naam', 'raj', 'hai']
# print(result[0])  # mera  — pehla word
# print(result[1])  # naam  — doosra word
# print(result[2])  # raj   — teesra word
# print(result[3])  # hai   — chautha word



# # line seprator 
# text = """This is Swati.
# This is Sanchit.
# This is Anshul.
# This is Anoop."""
# print(text.split('\n'))

# text = "This is Swati.\nThis is Sanchit.\nThis is Anshul.\nThis is Anoop."
# lines = (text.split('\n'))  # ["This is Swati" , "This is Sanchit" , "This is Anshul" , "This is Anoop"]
# print(lines[0])
# print(lines[1])
# print(lines[2])
# print(lines[3])
# print(lines[1:]) # index 1 se last tk 
# print(lines[1:][-1]) # 0 index skip ho gya and last ka print hoga 


# # join() — List ko String banana

# lines = ['hello', 'world', 'bye']

# result = ' '.join(lines)
# print(result)  # hello world bye

# lines = ['hello', 'world', 'bye']

# print(' '.join(lines))    # hello world bye
# print('-'.join(lines))    # hello-world-bye
# print('...'.join(lines))  # hello...world...bye

line1 = "   "
line2 = "hello"
line3 = "  ec2-user  "

print(bool(line1.strip()))  # False # empty 
print(bool(line2.strip()))  # True "hello"
print(bool(line3.strip()))  # True "ec2-user"