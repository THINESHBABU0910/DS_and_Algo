#Seive Theorm to see the prime numbers from the number given

#like N=50 means we will see the prime numbers from 1 to 50


from math import *

def genprime(n):
    primes = [True] *(n+1)
    primes[0]= False #Because 0 and 1 are not prime numbers
    primes[1]= False 

    for p in range(2, int (sqrt(n))+1):
        if primes[p] == True:
            for i in range(p*p,n+1,p):
                primes[i] = False
    

    for i in range(0,len(primes)):
        if primes[i] == True:
            print(i, end=' ')
    


t = int(input())
while t:
    n = int(input())
    genprime(n)
    t=t-1