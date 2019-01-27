R1 = list(map(int,input().split()))
R2 = list(map(int,input().split()))
A1 = R1[0]*R1[1]
A2 = R2[0]*R2[1]
if A1>A2:
    R = "Primeiro"
elif A1 == A2:
    R = "Empate"
else:
    R = "Segundo"
print(R)