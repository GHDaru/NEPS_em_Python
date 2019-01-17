A = [int(input()) for i in range(4)]
B = [ A[i]*A[i+1] for i in [0,2]]
print(B[0] if B[0]>B[1] else B[1])