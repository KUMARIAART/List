a=[1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
i=0
j=20
k=30
b=[]
count=0
innercount=1
while i<len(a):
    if count==2:
        if innercount==1:
            b.append(j)
            innercount+=1
        elif innercount==2:
            b.append(k) 
            innercount=1
        count=0
    b.append(a[i]) 
    count+=1
    i+=1
print(b)  