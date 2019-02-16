N,M = list(map(int,input().split()))
M1 = max(N - 2*M,1)
R = 0
if M1 > M:
    R = 0
else:
    for i in range(M1, M + 1):
        Min = max(N - M - i,1)
        Max = min( M , N - i - Min)
        R += Max - Min  + 1
        #print(i,Min,Max,R)
print(R)
