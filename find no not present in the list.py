list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7]
i=0
j=[]

while i<len(list1): 
        a=list1[i]
        if a not in list2:
            j.append(a) 
        i+=1
print(j)
