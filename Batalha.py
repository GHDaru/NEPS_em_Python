R = [int(input()) for i in range(4)]

D = [ R[0]!=R[3] and R[2]==R[1], R[0]==R[3] and R[2]!=R[1],]
#print(D)
print((D[0] == D[1])*(-1) + (D[0]*1 + D[1]*2)*(1-(D[0]==D[1])))

