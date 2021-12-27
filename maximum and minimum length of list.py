number=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
i=0
count=0
max_lenght=number[i]
while i<len(number):
    b=number[i]
    if b>max_lenght:
        max_lenght=b
    i+=1
print("maximum lenght list is:",max_lenght)
i=0
minimum_lenght=number[i] 
while i<len(number):
    b=number[i] 
    if b<minimum_lenght:
        minimum_lenght=b
    i+=1
print("minumum lenght list is :",minimum_lenght)           


number=[ [0],[1, 3], [5, 7], [9, 11], [13, 15, 17]]
i=0
count=len(number[i])
a=[]
max_lenght=number[i]
while i<len(number):
    b=number[i]
    if b>max_lenght:
        max_lenght=b
        count=len(max_lenght)
    i+=1
print("maximum lenght list is:","(",count,max_lenght,")")
i=0
count=len(number[i])
minimum_lenght=number[i] 
while i<len(number):
    b=number[i] 
    if b<minimum_lenght:
        minimum_lenght=b
        count=len(minimum_lenght)
    i+=1
print("minumum lenght list is :","(",count, minimum_lenght,")")         


