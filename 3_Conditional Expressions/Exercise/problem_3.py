# A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams. 

p1 = "Make a lot of money"
p2 = "nuy now"
p3 = "subscribe this"
p4 = "click this"

comment = input("Enter your comment: ")

if (p1 in comment) or (p2 in comment) or (p3 in comment) or (p4 in comment):
    print("This comment is spam.")

else:
    print("This comment is not spam")