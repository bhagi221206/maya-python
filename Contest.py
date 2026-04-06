X, A, B = map(int, input().split())
total = A + (2 * B)
if total >= X:
    print("Qualify")
else:
    print("Not Qualify")
