n=int(input())
star=[]
for i in range(n):
    str1=" "*i+"*"*(2*n-2*i-1)
    print(str1)
    star.append(str1)
star.remove(star[-1])
for i in range(n-1):
    print(star[n-i-2])