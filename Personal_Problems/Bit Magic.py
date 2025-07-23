#bitwise operator and - &
#bitwise operator or - |
#bitwise operator not - ~
#bitwise operator xor - ^
#bitwise operator right shift - >>
#bitwise operator left shift - <<




def evenodd(n):
    if n&1 ==1:
        return "Odd"
    else:
        return "Even"

def mulpow2(x,y):
    return x << y  # x * (2 ** y)

def divpow2(x,y):
    return x >> y  # x // (2 ** y)
    

t = int(input())
while t:
    n = int(input())
    m = evenodd(n)
    print(m)
    x,y = map(int, input().split())
    print(mulpow2(x,y))
    print(divpow2(x,y))
    t-=1