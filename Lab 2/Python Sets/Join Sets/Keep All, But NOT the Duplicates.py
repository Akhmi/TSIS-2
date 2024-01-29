x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x) #{'microsoft', 'google', 'banana', 'cherry'}

#Ex2

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z) #{'banana', 'microsoft', 'google', 'cherry'}

#Ex3

x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)

print(z) #{2, 'google', 'banana', 'cherry'}