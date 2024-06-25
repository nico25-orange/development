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

# 成績向上のための計算
target_average = 90 # 目標平均点
total_points_needed = target_average * 3 - sum_score  # 全教科で必要な総点数
additional_points_per_subject = total_points_needed / 3  # 各教科で必要な追加点数

print(f"各教科で平均点{target_average}に到達するために必要な追加点数: {additional_points_per_subject}")
