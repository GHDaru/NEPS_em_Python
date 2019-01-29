#https://pt.wikipedia.org/wiki/Teorema_do_n%C3%BAmero_primo

import math


def SieveOfEratosthenes(N, prime):
    prime[0] = False
    prime[1] = False

    for i in range(2, int(MAX**(1/2))):
        if prime[i]==True:
            for j in range(i*i,N+1,i):
                prime[j]=False
    return prime




# nth prime
def nthprime(N):
    i = 1
    cont = 0
    nth = 2
    while cont < N and i <= len(prime):
        # print(i,prime[i],cont, nth, N)
        if prime[i] == True:
            cont += 1
        i += 1
    nth = i - 1
    return nth


# Driver code
# create the sieve

N = int(input())
MAX = math.ceil(math.exp(1.163 * math.log(N) + 1))
# print(MAX)
prime = [True for i in range(MAX + 1)]
prime = SieveOfEratosthenes(MAX, prime)
print(nthprime(N))

# for i in range(2,MAX+1):
#    if prime[i]==True:
#        print(i,end=" ")


