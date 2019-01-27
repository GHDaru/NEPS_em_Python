Duracao = []
while True:
    X = list(map(int,input().split()))
    HI = X[0]*60+X[1]
    HF = X[2]*60+X[3]
    if HF == 0 and HI == 0:
        break
    HF += 24*60 if HF <= HI else 0
    Duracao.append(HF - HI)
print(*Duracao, sep = '\n')