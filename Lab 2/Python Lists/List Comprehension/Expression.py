fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]

#Ex2

newlist = ['hello' for x in fruits]

#Ex3

newlist = [x if x != "banana" else "orange" for x in fruits]