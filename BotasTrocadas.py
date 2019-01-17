N = int(input())
B = {}
QB = 0
for i in range(N):
    T = input().split()
    if T[0] not in B:
        B[T[0]] = {'E':0,'D':0}
    B[T[0]][T[1]] += 1
M = [(bota['E'] if bota['E']<=bota['D'] else bota['D']) for bota in B.values()]
print(sum(M))
