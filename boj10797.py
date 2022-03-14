#10부제 차량문제
a=input()
cars=list(map(str,input().split()))
cnt=int(0)
for i in cars:
    num=list(i)[-1]
    if num==a:
        cnt+=1
print(cnt)