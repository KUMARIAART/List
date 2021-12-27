elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
counter=0
even=0
odd=0
while counter <(len(elements)):
    if elements[counter] % 2==0:
        even+=1
        print (elements[counter],"is even number")
    else:
        odd+=1
        print (elements[counter],"is odd number")
    counter=counter+1     
print("total number of even:",even)
print("total number of odd:", odd)   
