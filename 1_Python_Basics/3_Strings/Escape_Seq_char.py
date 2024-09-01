#  Escape Sequence Characters

# Sequence of characters after backslash "\" → Escape Sequence characters 
# Escape Sequence characters comprise of more than one character but represent one 
# character when used within the strings.

#  \n -> new line

a = "Python is easy to learn\nbut not so easy"
print(a)

# \t -> Tab space

b = "Python is easy to learn\n\tbut not so easy"
print(b)

# \' -> for single quote.

c = "Python is easy to learn \"but\" not so easy"
print(c)

# Same as

d = "Python is easy to learn 'but' not so easy"
# OR
e = 'Python is easy to learn "but" not so easy'

print(c)
print(d)
print(e)

# \\ -> use for adding backslash

f = "Python is easy to learn\\ but not so easy"
print(f)