elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
counter=0
sum1=0
sum2=0
count1=0
count2=0
while counter <(len(elements)):
    if elements[counter] % 2==0:
        sum1=sum1+elements[counter]
        count1+=1    
    else:
        sum2=sum2+elements[counter]
        count2+=1 
    counter+=1            
print (sum1/count1,"is avreage of even number")
print (sum2/count2,"is avreage of odd number")
        
  