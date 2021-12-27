list=[12, 45, 23, 67, 78, 90, 45, 32, 100, 76 ,12,34]
list1 = []
i = 0
while i < len(list):
    j = 0
    list2 = []
    k = i
    while j< 3:
        list2.append(list[k])
        print(list[k])
        j+=1
        k+=1
    list1.append(list2)
    i+=3
print(list1)











# i=0
# k=0
# while i< (len(list)/2):
#     j = 0
#     s = []
#     while j < 2:
#         if k == 15:
#             break
#         if j < 5 :
#             s.append(list[k]) 
#         j+=1
#         k+=1
#     list1.append(s)
#     i+=1
# print(list1)



