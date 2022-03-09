str1=input()
croa=["c=","c-","dz=","d-","lj","nj","s=","z="]
for i in croa:
    if i in str1:
        str1=str1.replace(i,"1")
print(len(str1))