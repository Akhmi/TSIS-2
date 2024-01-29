set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3) #{1, 2, 3, 'b', 'a', 'c'}

#Ex2

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1) #{1, 2, 3, 'c', 'a', 'b'}