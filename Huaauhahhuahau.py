Risada = input()
vogais = ['a','e','i','o','u']
NovaRisada = []
#Extrai vogais
for i in Risada:
    if i in vogais:
        NovaRisada.append(i)
NovaRisada = ''.join(NovaRisada)
RisadaInvertida = NovaRisada[len(NovaRisada)::-1]
if NovaRisada == RisadaInvertida:
    Resp = "S"
else:
    Resp = "N"
print(Resp)