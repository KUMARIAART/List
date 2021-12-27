test_list=[4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
i=0
a=[]
while i<len(test_list):
    j=0
    count=0
    while j<len(test_list):
        if test_list[i]==test_list[j]:
            count=count+1
        j=j+1
        if count>=3:
            if test_list[i] not in a:
                a.append (test_list[i])
    i=i+1
print(a)


test_list=[4, 6, 4, 3, 3, 4, 3, 4, 6, 6]
i=0
a=[]
while i<len(test_list):
    j=0
    count=0
    while j<len(test_list):
        if test_list[i]==test_list[j]:
            count=count+1
        j=j+1
        if count>=3:
            if test_list[i] not in a:
                a.append (test_list[i])
    i=i+1
print(a)


