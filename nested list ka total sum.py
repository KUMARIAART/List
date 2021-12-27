number=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
i=0
a=[]
sum=0
while i<len(number):
    if type(number[i])==list:
        j=0
        while j<len(number[i]):
            if type(number[i][j])==list:
                k=0
                while k<len(number[i][j]):
                    a.append (number[i][j][k])
                    sum=sum+number[i][j]
                    k+=1
            else:
                a.append(number[i][j]) 
                sum=sum+number[i][j] 
            j+=1
    else:
        a.append(number[i]) 
        sum=sum+number[i]  
    i+=1
print(a) 
print(sum)       


