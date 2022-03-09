n=int(input())
num_list=[]
for i in range(n):
    input_num=int(input())
    num_list.append(input_num)
    
num_list.sort()
for j in range(n):
    print(num_list[j])