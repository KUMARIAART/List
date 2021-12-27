elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
counter=0
sum1=0
sum2=0
while counter <(len(elements)):
    if elements[counter] % 2==0:
        sum1=sum1+elements[counter]
    else:
        sum2=sum2+elements[counter] 
    counter+=1            
print (sum1,"is even number")
print (sum2,"is odd number")




        
  

