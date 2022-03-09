n=int(input())
tf=int(0)
cnt=int(0)
for t in range(n):
    is_group=list(input())
    is_group_rev=is_group[::-1]
    while(len(is_group)!=0):
        i=is_group[0]
        removeSet={i}
        x=is_group.index(i)
        y=len(is_group)-is_group_rev.index(i)-1
        if is_group.count(i)==(y-x+1):
            tf=1
            is_group=[k for k in is_group if k not in removeSet]
        else:
            tf=0
            break;
    if tf==1:
        cnt+=1
    else:
        cnt+=0
print(cnt)