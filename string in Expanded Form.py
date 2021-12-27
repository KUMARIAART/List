s=int(input("enter any number:-"))
b=1
a=[]
while b<=s:
    n=int(input("enter any number:-"))
    a.append(n)
    b+=1
i=0
while i<len(a):
    rem=a[i]//1000%100
    c=a[i]//10000
    sum=c*10000
    c1=rem*1000
    rem1=a[i]//100%100
    c2=a[i]//1000
    sum1=c2*1000
    c3=rem1*100
    rem2=a[i]%100
    i=i+1
print(c1,"+",c3,"+",rem2)

s=int(input("enter any number:-"))
b=1
a=[]
while b<=s:
    n=int(input("enter any number:-"))
    a.append(n)
    b+=1
i=0
rem=0
sum=0
while i<len(a):
    rem=a[i]%10
    sum=a[i]//10
    sum=sum*10
    i=i+1
    print(sum,"+",rem)






    


    

