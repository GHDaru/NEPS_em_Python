N = int(input())
V = list(map(float,input().split()))
print( '{:.2f}'.format( (V[N-1]-V[0])*100  ))