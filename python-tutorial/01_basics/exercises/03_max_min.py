# 生徒のテストの点数
math_score = 85
science_score = 90
history_score = 75

# 平均点の計算
sum_score = math_score + science_score + history_score
average_score = sum_score / 3

# テストの点数と平均点の表示
print(f"数学の点数: {math_score}")
print(f"理科の点数: {science_score}")
print(f"歴史の点数: {history_score}")
print(f"3教科の平均点: {average_score}")

max_score = max(math_score, science_score, history_score)
min_score = min(math_score, science_score, history_score)

print(f"3教科の中で最高点は{max_score}点です。")
print(f"3教科の中で最低点は{min_score}点です。")
