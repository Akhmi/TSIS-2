thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset) #{'apple', 'cherry'}


#Ex2

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset) #{'cherry', 'apple'}


#Ex3

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x) #apple

print(thisset) #{'banana', 'cherry'}


#Ex4

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset) #set()


#Ex5

thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset) #error