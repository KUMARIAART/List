a=[1,2,3]
i=0
while i<len(a):
    j=0
    while j<len(a):
        k=0
        while k<len(a):
            if i!=j and j!=k and i!=k:
                print(a[i],a[j],a[k])
            k=k+1 
        j=j+1
    i=i+1           

                



