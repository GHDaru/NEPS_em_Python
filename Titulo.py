# def PrimMaiuscula(x):
#     Palavras = x.split()
#     for i in range(len(Palavras)):
#         Palavras[i] = Palavras[i][0].upper() + Palavras[i][1:]
#     return ' '.join(Palavras)
# V = input()
# print(PrimMaiuscula(V))

#Versão sem função
# V = input().split()
# F = [V[i][0].upper() + V[i][1:] for i in range(len(V))]
# print(' '.join(F))
# print(V[0].capitalize())
V = input().split()
F = [V[i].capitalize() for i in range(len(V))]
print(' '.join(F))