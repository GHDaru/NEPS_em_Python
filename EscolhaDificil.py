C = list(map(int,input().split()))
D = list(map(int,input().split()))
R = [ D[i]-C[i] if D[i]-C[i] > 0  else 0 for i in range(len(C)) ]
print(sum(R))
