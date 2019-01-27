def mdc(a,b):
    if b == 0:
        return a
    else:
        return mdc(b, a%b)


#print(mdc(2,2), mdc(6,3), mdc(21,0), mdc(50,30), mdc(30,50))

N = int(input())
V = input().split()
MDCS = int(V[0])
for i in V[1:len(V)+1]:
    MDCS = mdc(int(i), MDCS)
print(MDCS)