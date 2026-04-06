rolls = list(map(int, input().split()))
A = rolls[:3]
B = rolls[3:]
alice_score = sum(sorted(A, reverse=True)[:2])
bob_score = sum(sorted(B, reverse=True)[:2])
if alice_score > bob_score:
    print("Alice")
elif bob_score > alice_score:
    print("Bob")
else:
    print("Tie")
