import math
n=int(input())
fac=math.factorial(n)
cnt=0
l1=list(str(fac))
l=len(l1)-1
while True:
    if l1[l]=='0':
        cnt+=1
        l-=1
    else:
        break;
print(cnt)