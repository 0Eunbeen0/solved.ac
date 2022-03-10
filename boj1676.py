n=int(input())
fac=int(1)
zero_count=int(0)
for i in range(n):
    fac=fac*(i+1)
while(fac%10==0):
    zero_count+=1
    fac/=10
print(zero_count)