list=[1, 2, 3, 4, 5, 6]
list1 = []
i=1
k = 0
while i<len(list):
    list1.append([list[k],list[i]])
    i+=1
    k+=1
print(list1)