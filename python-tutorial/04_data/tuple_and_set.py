# タプルは追加、削除、修正などの変更不可
cars = ("Prius", "Estima", "Voxy", "Noah")

# 集合
fruits = {"apple", "banana", "orange"}
fruits.add("apple")
print(fruits)

# 集合同士の演算
a = {1, 2, 3}
b = {1, 2, 4, 5}

# aとbの和集合
print(a | b)

# aとbの積集合
print(a & b)

duplicated_alphabets = ["a", "a", "b", "c"]
unique_alphabets =  set(duplicated_alphabets)
