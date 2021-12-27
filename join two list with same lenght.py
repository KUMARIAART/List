Original_lists1=[[10, 20], [30, 40], [50, 60], [30, 20, 80]]
Original_lists2=[[61], [12, 14, 15], [12, 13, 19, 20], [12]]
i=0
j=[]
while i<len(Original_lists1):
    a=(Original_lists1[i]+(Original_lists2[i])) 
    j.append(a) 
    i+=1
print(j)   


Original_lists1=[['a', 'b'], ['b', 'c', 'd'], ['e', 'f']]
Original_lists2=[['p', 'q'], ['p', 's', 't'], ['u', 'v', 'w']]
i=0
j=[]
while i<len(Original_lists1):
    a=(Original_lists1[i]+(Original_lists2[i])) 
    j.append(a) 
    i+=1
print(j)
