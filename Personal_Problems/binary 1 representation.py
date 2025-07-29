#returns no of 1's in binary representation of a number in int.
# 5 -> 101  ans = 2
# 7 -> 111 ans = 3

#2 approaches:
#brute force 
#T.C = 0(n)
# def bruteforcecntbits(n):
#     s= str(bin(n))[2:]
#     # print("{}",s)
#     return s.count('1')


def cntbits(n):
    cnt = 0
    while n:
        cnt +=1
        n = n & (n -1)
    return cnt

t= int(input())
while t:
    n = int(input())
    # print(bruteforcecntbits(n))
    print(cntbits(n))
    t-=1

