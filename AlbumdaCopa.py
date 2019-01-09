N = int(input())
M = int(input())
F = []
for i in range(M):
    F.append(int(input()))
print(N - len(set(F)))