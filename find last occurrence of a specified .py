original_list=['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
a=[]
i=0
while i<len(original_list):
    c=0
    j=0
    while j<len(original_list):
        if original_list[i]==original_list[j]:
            c=j
        j+=1
    if original_list[i]  in a:
        i+=1
        continue
    a.append(original_list[i])
    print(original_list[i],"=",c)       