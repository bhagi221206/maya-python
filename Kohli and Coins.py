X = int(input())
if X % 5 != 0:
    print(-1)
else:
    coins = X // 10 + (1 if X % 10 == 5 else 0)
    print(coins)
