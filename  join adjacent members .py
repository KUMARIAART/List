list=['1', '2', '3', '4', '5', '6', '7', '8']
list1 = []
i=0
k=1
while i<len(list):
    sum=""
    sum = sum +list[i]+list[k]
    i+=2
    k+=2
    list1.append(sum)
print(list1)