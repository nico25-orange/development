cars = ["Prius", "Estima", "Voxy", "Noah"]

# 要素は0から始まる。

prius = cars[0]
noah = cars[3]
print("(1)")
print(prius)
print(noah)

# 後ろからn番目はcars[-n]
print("(2)")
print(cars[-1]) # Noah

# forでループさせることができる。
print("(3)")
for car in cars:
    print(car)

cars.append("Alphard")
print("(4)")
print(cars)

# リストの長さを求める。
print(f"carsの長さは{len(cars)}")

cars.remove("Voxy")
print("(5)")
print(cars)

cars.reverse()
print(cars)

print("(6)")
# 配列の中にある数値の合計をsum関数で求めることができる。
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(numbers))