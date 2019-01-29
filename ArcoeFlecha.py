def mergeSort(lista):

    pen = 0
    if len(lista) > 1:

        meio = len(lista)//2
        #também é valido: meio = int(len(lista)/2)

        listaDaEsquerda = lista[:meio]
        listaDaDireita = lista[meio:]

        pen += mergeSort(listaDaEsquerda)
        pen += mergeSort(listaDaDireita)

        i = 0
        j = 0
        k = 0

        while i < len(listaDaEsquerda) and j < len(listaDaDireita):

            if listaDaEsquerda[i] <= listaDaDireita[j]:
                lista[k]=listaDaEsquerda[i]
                i += 1
                pen += len(listaDaDireita) - j
            else:
                lista[k]=listaDaDireita[j]
                j += 1
            k += 1

        while i < len(listaDaEsquerda):

            lista[k]=listaDaEsquerda[i]
            i += 1
            k += 1

        while j < len(listaDaDireita):
            lista[k]=listaDaDireita[j]
            j += 1
            k += 1
    return pen




def dist(T):
    return (T[0]**2 + T[1]**2)**(1/2)

N = int(input())
#C contém as coordenadas em formato de lista dos tiros
D = [ dist(list(map(int,input().split()))) for i in range(N) ]
pen = mergeSort(D)
#D contém as distâncias de cada tiro
#D = list(map(dist, C))
#Cálculo das penalidades
print(pen)
# PT = 0
# for j in range(1,N):
#     for i in range(j):
#         PT += 1 if D[i] <= D[j] else 0
# print(PT)
#print(C)
#print(D)
