Q = [int(input()) for i in range(3)]
M = min([2*Q[1]+4*Q[2], 2*(Q[0]+Q[2]), 4*Q[0]+2*Q[1]])
print(M)
