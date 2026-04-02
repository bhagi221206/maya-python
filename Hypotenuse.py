import math
x, y = map(int, input().split())
hypotenuse = math.sqrt(x**2 + y**2)
print(f"{hypotenuse:.2f}")
