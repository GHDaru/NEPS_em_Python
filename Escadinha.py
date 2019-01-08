#https://neps.academy/problem/165
N = int(input())
V = list(map(int,input().split()))
T = V[0:-1]
for i in range(0,len(T)):
    T[i] = V[i+1] - V[i]
#print(T)
escadinha = 1
for i in range(1,len(T)):
    escadinha += 1 if T[i]!=T[i-1] else 0
print(escadinha)