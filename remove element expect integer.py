original_list=[34.67, 12, -94.89, 'Python', 0, 'C#']
i=0
while i<len(original_list):
    if type(original_list[i]) == str:
        print(original_list[i])
    i+=1

