N, C, S = list(map(int,input().split()))
O = list(map(int,input().split()))
P = 0
S -= 1
V = 1 if P == S else 0
for i in O:
    P = (P + i ) % N
    V += 1 if P == S else 0
print(V)

