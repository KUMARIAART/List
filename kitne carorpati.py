kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i=0
while i<len(kitna_paisa_hai):
    if kitna_paisa_hai[i]>=10000000:
        print(kitna_paisa_hai[i],"Crorepati")
    elif kitna_paisa_hai[i] >=100000:
        print(kitna_paisa_hai[i],"lakhpati") 
    else:
        print(kitna_paisa_hai[i],"dilwale")                
    i+=1