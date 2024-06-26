import random

def generate_random_number():
    # 1から10のランダムな整数を生成
    random_number = random.randint(1, 10)
    return random_number

# 関数を呼び出してランダムな数を出力
print(generate_random_number())
