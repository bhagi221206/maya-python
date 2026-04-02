Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import sys
... 
... data = list(map(float, sys.stdin.read().strip().split()))
... p = data[0]
... r = data[1]
... t = data[2]
... a = p * (1 + r / 100) ** t
... ci = a - p
