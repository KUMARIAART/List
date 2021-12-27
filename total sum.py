number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19]
i=0
j=[]
while i<len(n):
    s=0
    while i>s:
        if n[i]+n[s]==number:
            j.append ([n[i],n[s]])    
        s+=1 
    i+=1    
print(j)



