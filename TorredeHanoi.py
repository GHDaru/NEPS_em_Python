# def Hanoi(N, Orig, Dest, Temp,Cont):
#      if N == 1:
#         #print("Move disco do pino:", Orig, 'para o disco', Dest, 'usando o disco', Temp, 'para',N,'discos')
#         Dest.append(Orig.pop());
#         Cont+=1;
#      else:
#         Cont = Hanoi(N - 1, Orig, Temp, Dest, Cont)
#         #mover o N-ésimo menor disco do pino Orig para o pino Dest;
#         #print("Move disco do pino:", Orig, 'para o disco', Dest, 'usando o disco', Temp, 'para', N, 'discos')
#         Dest.append(Orig.pop());
#         Cont += 1
#         Cont = Hanoi(N-1, Temp, Dest, Orig, Cont);
#      return Cont
#
# E = list(map(int,input().split()))
# #último elemento é zero
# for i in range(0,len(E)-1):
#     Orig = list(range(len(E)-1,-1, -1))
#     Dest = []
#     Temp = []
#     Cont = 0
#     Cont = Hanoi(E[i], Orig, Dest, Temp, Cont)
#     print('Tarefa',i+1)
#     print(Cont)
E = list(map(int,input().split()))
#último elemento é zero
for i in range(0,len(E)-1):
    print('Tarefa', i + 1)
    print(2**E[i]-1)