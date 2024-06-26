def is_prime(n):
    # 1以下の数は素数ではない
    if n <= 1:
        return False
    # 2は素数である
    if n == 2:
        return True
    # 2以外の偶数は素数ではない
    if n % 2 == 0:
        return False
    # 3からnの平方根までの奇数で割り切れるかをチェック
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

for i in range(15):
    if is_prime(i):
        print(f"{i}は素数です。")
    else:
        print(f"{i}は素数ではありません。")
