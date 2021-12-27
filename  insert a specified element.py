a=[1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
i=0
j=[]
k = 0
while i<len(a):
    if k==2:
        j.append(a[i]) 
        j.append (20)
        k-=2
    else:
        j.append(a[i])
        k+=1
    i+=1 
print(j)     


