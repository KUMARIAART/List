a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b=[]
c=1
i=0
while i<len(a) and c<len(a):
    d=a[c]-a[i]
    b.append(d)
    c+=1
    i+=1
print(b) 


a=[2, 4, 6, 8]
b=[]
c=1
i=0
while i<len(a) and c<len(a):
    d=a[c]-a[i]
    b.append(d)
    c+=1
    i+=1
print(b)

