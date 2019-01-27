N, M = list(map(int,input().split()))
R = list(map(int,input().split()))
T = [0]*M
for i in R:
    T[i-1]+=1
print(min(T))

