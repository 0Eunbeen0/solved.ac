import sys
m,n=map(int,sys.stdin.readline().split())
div=int(2)
while(m<=n): 
    t=m%div
    if t==0 and div!=m:
        m+=1
        div=int(2) 
    elif t==0 and div==m:
        print(m)
        m+=1
        div=int(2)
    else:
        div+=1