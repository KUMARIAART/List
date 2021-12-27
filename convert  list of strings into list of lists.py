O=['Red', 'Maroon', 'Yellow', 'Olive']
# s = []
# i = 0
# while i <len(O):
#     s.append(list(O[i]))
#     i+=1
# print(s)

s = []
i = 0
while i <len(O):
    j=[]
    k=0
    while k<len(O[i]):
        j.append(O[i][k])
        k+=1
    s.append (j)    
    i+=1
print(s)