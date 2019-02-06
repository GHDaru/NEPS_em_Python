N = int(input())
C = list(map(int,input().split()))
E = set()
P = 0
for i in C:
    if i in E:
        E.remove(i)
    else:
        P += 2
        E.add(i)
print(P)
