Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import sys
... data = sys.stdin.read().strip().split()
... N = int(data[0])
... M = int(data[1])
... total_people = (N * 5) + (M * 7)
