# 好きな数を選ぶ
target_number = 54

# ユーザーが数を当てるまで続ける
while True:
    guess = int(input("1から100までの数を当ててみてください: "))
    if guess < target_number:
        print("小さいです。")
    elif guess > target_number:
        print("大きいです。")
    else:
        print("正解です！")
        break

