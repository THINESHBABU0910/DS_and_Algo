from math import *
def fun(n):
    div1 = set()
    for i in range(1, int(sqrt(n))+1):
        if n % i ==0:
            div1.add(i)
            div1.add(n//i)
            
    return list(div1)

t= int(input())
while t:
    n= int(input())
    div1 = fun(n)
    print(*div1)  # need output as list then remove that * else it will give output as 1 2 3  
t -=1

