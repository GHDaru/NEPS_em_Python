v = [0,0,0,0,0,0]
for i in range(6):
    v[i] = int(input())
#Converte para segundos
T1 = v[0]*24*60*60+v[1]*60*60+v[2]*60
T2 = v[3]*24*60*60+v[4]*60*60+v[5]*60
DT = T2-T1
print(DT)