N = int(input())
V = list(map(int,input().split()))
T = sum(V)//2
S = V[0]
for i in range(1,len(V)):
    S+=V[i]
    if S >= T:
        R = i
        break
print(R+1)