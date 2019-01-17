Ia,Ib, Fa, Fb = input().split()
if Ia == Fa and Ib == Fb:
#Se estados são iguais nada a fazer
    Apertos = 0
elif Ia == Fa and Ib!=Fb:
#Se o estado de B está diferente e o de A já está igual,  deve-se aperta o interruptor B para levar B
#ao estado final, porém o A agora não está mais no estado final, devendo apertar-se o interruptor A
    Apertos = 2
else:
#Sobrou os estados de ambos totalmente opostos (só apertar B) ou
#Somente A invertido, apertar interruptor A
    Apertos = 1
print(Apertos)