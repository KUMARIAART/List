List = [6,1,3,5,6,3,1]
i=0
j=[]
k=0
while i<len(List):
    if List[i] not in j:
        j.append(List[i])
        k=k*(List[i])
        k+=1
    i+=1
print(j,"\n","List product is=",k)






    
    

