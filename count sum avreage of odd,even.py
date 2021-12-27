elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
counter=0
even=0
odd=0
sum1=0
sum2=0
while counter <(len(elements)):
    if elements[counter] % 2==0:
        sum1=sum1+elements[counter]
        even+=1
    else:
        sum2=sum2+elements[counter] 
        odd+=1
    counter=counter+1     
print(even,"total number of even:")
print(odd,"total number of odd:") 
print(even+odd,"count of the all  number")
print (sum1,"sum of even number")
print (sum2,"sum of odd number")
print(sum1+sum2,"sum of the all number")
print (sum1/even,"is avreage of even number")
print (sum2/odd,"is avreage of odd number")
print(counter/even+counter/odd,"avrege of all numbers")
     

