n,p=map(int,input().split())
d=[n]
gap=int()
overlap=int()
while(True):
    num_list=list(str(d[-1]))
    x=int(0)
    for i in num_list:
        x+=int(i)**p
        if d.count(i)>1:
            overlap=d.index(i)
            gap=d.index(j,overlap+1)-overlap
            break;
        else:
            d.append(x)
            print(d)
            
length=len(x)
del x[length-gap:]
print(length)  