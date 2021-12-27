a=(2,3,4,5,6,7,8)
counter=0
even=0
odd=0
while counter <(len(a)):
    if a[counter] % 2==0:
        even+=1
        print (a[counter],"is even number")
    else:
        odd+=1
        print (a[counter],"is odd number")
    counter=counter+1 
print("total number of even:",even)
print("total number of odd:", odd)   


# day=int(input("Enter the date:"))
# month=input("enter the month:")
# if(day>=1 and day<=31) and (month=="july" or month=="april"):
#     print("autumn")
    