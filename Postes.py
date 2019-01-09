N = int(input())
V = input().split()
T = [0,0,0]
for i in range(len(V)):
    T[0] += 1 if int(V[i]) < 50 else 0
    T[1] += 1 if int(V[i]) >= 50 and int(V[i])<85 else 0
    T[2] += 1 if int(V[i]) >= 85 else 0
print(T[0], T[1])


