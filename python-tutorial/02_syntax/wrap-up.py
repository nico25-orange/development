# 初期カウンターの設定
positive_count = 0
negative_count = 0
zero_count = 0

# ユーザーから数字の入力を求める
print("5つの数字を入力してください。各数字の後でEnterキーを押してください。")

# 5回繰り返す
for _ in range(5):
    number = int(input("数字を入力: "))
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1
    else:
        zero_count += 1

# 結果の表示
print(f"正の数: {positive_count}個")
print(f"負の数: {negative_count}個")
print(f"ゼロ: {zero_count}個")
