list=[5, 6, [], 3, [], [], 9]
i=0
j=[]
while i<len(list):
    if list[i]!=[]:
        j.append(list[i])
    i+=1
print(j)        

