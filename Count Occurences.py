char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
final=[]
i=0
l=[]
while i<len(char_list):
    j=0
    count=0
    while j<len(char_list):
        if char_list[i]==char_list[j]:
            count+=1
        j+=1
    if char_list[i] in l:
        i+=1
        continue
    l.append(char_list[i])
    print(char_list[i],"-",count,"times ")
    final.append([char_list[i],count])
print(final)







