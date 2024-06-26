# ユーザーから整数の入力を受ける
number = int(input("整数を入力してください: "))

# 偶数か奇数かを判断する
if number % 2 == 0:
    print(f"{number}は偶数です。")
else:
    print(f"{number}は奇数です。")
