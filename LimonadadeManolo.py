V = input().split()
N = int(V[0])
C = int(V[1])

if N >= C:
    Custo = (C + 1) * C / 2 + N - C
else:
    Custo = (C + C - N + 1) * (C - (C - N)) / 2
print(int(Custo))