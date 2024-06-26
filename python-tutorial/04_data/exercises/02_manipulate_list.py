# リストの作成
elements = [5, 9, 1, 3, 4, 8, 7]

# 特定の要素の位置を検索
index = elements.index(9)
print(f"要素9の位置: {index}")

# リストの末尾に要素を追加し、最初の要素を削除
elements.append(10)
removed_element = elements.pop(0)
print(f"追加後と削除後のリスト: {elements}")

# リストの要素を逆順にする
elements.reverse()
print(f"逆順のリスト: {elements}")

# リストの要素をソートする
elements.sort()
print(f"ソートされたリスト: {elements}")
