N = int(input())
V = input().split()
seq = 1
ant = V[0]
maior = 1
for i in V[1:len(V)]:
    seq = (seq + 1) if ant == i else 1
    maior = seq if seq > maior else maior
    ant = i
    #print(seq, maior, i)
print(maior)