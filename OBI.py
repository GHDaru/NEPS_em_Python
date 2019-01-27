N,P = list(map(int,input().split()))
S = [ list(map(int,input().split())) for i in range(N) ]
A = [ S[i][0] + S[i][1] >= P for i in range(N) ]
print(sum(A) )
