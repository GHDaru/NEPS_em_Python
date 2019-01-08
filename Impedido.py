V = list(map(int,input().split()))
L = V[0]
R = V[1]
D = V[2]
if R > 50 and L < R and R > D :
    Resp = "S"
else:
    Resp = "N"
print(Resp)