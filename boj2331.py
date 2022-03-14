n,p=map(int,input().split())
d=[n]
gap=int()
overlap=int()
while(True):
    num_list=list(str(d[-1]))
    x=int(0)
    for i in num_list:
        x+=int(i)**p
    d.append(x)
    if d.count(x)>=2:
        overlap=d.index(x)
        gap=d.index(x,overlap+1)-overlap
        break;
length=len(d)
print(length-gap-1)