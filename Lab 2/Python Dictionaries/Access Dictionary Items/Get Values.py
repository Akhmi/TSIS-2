#x = thisdict.values()

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change   #dict_values(['Ford', 'Mustang', 1964])

car["year"] = 2020

print(x) #after the change   #dict_values(['Ford', 'Mustang', 2020])



#Ex2

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change   #dict_values(['Ford', 'Mustang', 1964])

car["color"] = "red"

print(x) #after the change   #dict_values(['Ford', 'Mustang', 1964, 'red'])