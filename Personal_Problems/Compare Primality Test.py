from math import *
def approach1(n):   #O(n)
    divcount =0
    for i in range(1,n+1):
        if n%i == 0:
            divcount+=1
    
    print(divcount)
    if divcount ==2:
        return True
    else:
        return False


def approach2(n):  #O(root(n))
    if n == 0 or n ==1 :
        return False
    if n == 2 or n ==3:
        return True
    if n%2 ==0 or n%3 == 0:
        return False
    for i in range(5,int(sqrt(n))+1):
        if n%i == 0 or n%(i+2) == 0:
            return False
    return True

t = int(input())
while t:
    n = int(input())   
    print(approach1(n))
    print(approach2(n))

    t -= 1