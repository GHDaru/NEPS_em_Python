def chave(L):
    return int(L[1])
N,T = list(map(int,input().split()))
alunos = [ input().split() for i in range(N) ]
alunos.sort(key = chave, reverse=True)
times = [ [] for i in range(T)]
vez = -1
for i in alunos:
    vez = (vez + 1) % T
    times[vez].append(i[0])
for i in range(T):
    print('Time',i+1)
    times[i].sort()
    print(*(times[i]),sep='\n')
    print()
