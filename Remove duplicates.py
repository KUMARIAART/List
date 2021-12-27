list=[1,2,3,1,2,2]
i=0
j=[]
while i<len(list):
    if list[i] not in j:
        j.append(list[i])
    i+=1
print(j)        

