#Ex1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#apple
#banana
#cherry
  

#Ex2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#apple
#cherry
  

#Ex3
for x in range(6):
  print(x)
#0
#1
#2
#3
#4
#5
  

#Ex4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
#apple