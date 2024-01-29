fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green) #apple
print(yellow) #banana
print(red) #['cherry', 'strawberry', 'raspberry']

#Ex2

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green) #apple
print(tropic) #['mango', 'papaya', 'pineapple']
print(red) #cherry