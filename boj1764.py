import sys
people=[]
double_people=[]
n,m=map(int, sys.stdin.readline().split())
cnt=int(0)
for i in range(n+m):
    new_input=input()
    people.append(new_input)
    if people.count(new_input)==2:
        double_people.append(new_input)
        cnt+=1
double_people.sort()
print(cnt)
for i in double_people:
    print(i)