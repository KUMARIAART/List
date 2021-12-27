input_list = [1, 2, 2, 5, 8, 4, 4, 8]
i=0
j=[]
count=0
while i<len(input_list):
    if input_list[i] not in j:
        j.append(input_list[i])
        count+=1
    i+=1
print(j,"\n","count=",count)        
