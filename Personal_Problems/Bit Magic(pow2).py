
def powerof2(n):
    if n <= 0:
        return False
    x=n
    y=not(n & (n-1))
    # print(x, y)
    # print(" testL:", x and y)
    return x and y



t= int (input())

while t:
    n = int(input())
    print(powerof2(n))
    t-=1