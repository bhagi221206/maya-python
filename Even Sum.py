N = int(input())
arr = list(map(int, input().split()))
even_sum = sum(x for x in arr if x % 2 == 0)
print(even_sum)
