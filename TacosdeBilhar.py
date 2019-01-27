N = int(input())
C = list(map(int,input().split()))
E = []
P = 0
for i in C:
    if i in E:
        E.remove(i)
    else:
        P += 2
        E.append(i)
print(P)
