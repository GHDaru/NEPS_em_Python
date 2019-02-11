L,A,P,R = list(map(int,input().split()))
R = L*L + A*A + P*P <= 4*R*R
print( 'S' if R else 'N')