N = int(input())
E = list(map(int,input().split()))
M = int(input())
S = list(map(int,input().split()))
for i in S:
    E.remove(i)
print(*E)