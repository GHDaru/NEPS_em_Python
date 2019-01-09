V=[]
diagprin, diagsec = 0,0
for i in range(0,9):
    V.append(int(input()))
for i in range(0,3):
    for j in range(0,3):
        if i==j:
            diagprin += V[i*3 + j]
        if i+j == 2:
            diagsec += V[i*3 + j]
print("Diagonal principal:", diagprin)
print("Diagonal secundaria:", diagsec)