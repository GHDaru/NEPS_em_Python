N = int(input())
P1 = list(map(int,input().split()))
P2 = list(map(int,input().split()))
#É possível dividir na vertical se as coordenadas X estão um em uma metade e o outro na outra
Dividir_na_Vertical = (P1[0]<=N/2) != (P2[0]<=N/2)
#Similar regra para divisão na horizontal
Dividir_na_Horizontal = (P1[1]<=N/2) != (P2[1]<=N/2)
#Resposta se uma das divisões for possível então S senão N
print('S' if Dividir_na_Horizontal or Dividir_na_Vertical else 'N')
