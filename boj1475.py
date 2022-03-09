room_num=input()
num_list=list(room_num)
setNum=int(0)
print(num_list)
for  i in range(len(num_list)):
    if num_list[i]=="9":
        num_list[i]="6"

if num_list.count("6")<=2:
    for i in range(len(num_list)):
        if setNum<=num_list.count(num_list[i]):
            setNum=num_list.count(num_list[i])
        else:
            setNum=setNum
else:
    setNum=2
print(setNum)