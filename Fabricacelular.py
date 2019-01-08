N = int(input())
Q = input().split()
V = [0,0,0,0,0]
A = 0
B = 0
C = 0
for i in range(0,len(Q)):
    Q[i] =  int(Q[i])
    V[Q[i]-1]+=1
    if V[0]>0 and V[2]>0 and V[4]>0:
        A+=1
        V[0]-=1
        V[2]-=1
        V[4]-=1
    if V[0]>0 and V[3]>0:
        B+=1
        V[0]-=1
        V[3]-=1
    if V[1]>0 and V[3]>0:
        C+=1
        V[1]-=1
        V[3]-=1

print("A: "+str(A))
print("B: "+str(B))
print("C: " +str(C))