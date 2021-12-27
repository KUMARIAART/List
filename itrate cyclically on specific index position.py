original_list=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
start=int(input("enter the number where you start your list:"))
i=start
l=[]
while(i<len(original_list)):
    l.append(original_list[i])
    i+=1
a=0
k=[]
while(a<start):
    k.append(original_list[a])
    a+=1
print(l+k)


