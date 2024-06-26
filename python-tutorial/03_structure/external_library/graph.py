import matplotlib.pyplot as plt
plt.rcParams['font.family'] = "MS Gothic"

# 月ごとの売上データ
months = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]
sales = [200, 300, 250, 420, 520, 610, 500, 410, 620, 500, 450, 380]

# 折れ線グラフの作成
plt.figure(figsize=(10, 5))  # グラフのサイズ指定
plt.plot(months, sales, marker='o', color='b', linestyle='-')  # 折れ線グラフをプロット
plt.title('月ごとの売上')  # グラフのタイトル
plt.xlabel('月')  # x軸のラベル
plt.ylabel('売上（千円）')  # y軸のラベル
plt.grid(True)  # グリッドの表示

# グラフの表示
plt.show()
