students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
marks = [10, 20, 56, 45, 36, 20]
i=0
j=[]
while i<len(students):
    a=(students[i]+str(marks[i])) 
    j.append(a) 
    i+=1
print(students+marks)
print(j)   
