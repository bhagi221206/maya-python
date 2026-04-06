N = int(input())
arr = list(map(int, input().split()))
odd_index_sum = sum(arr[i] for i in range(N) if i % 2 != 0)
print(odd_index_sum)
