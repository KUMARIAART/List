numbers=[50,40,23,70,56,12,5,10,7]
i=0
max=0
while i<len(numbers):
    if numbers[i]>max:
        max=numbers[i]
    i=i+1
i=0
second_max=0
while i<len(numbers):
    if numbers[i]>second_max:
        if numbers[i]!=max:
            second_max=numbers[i]
    i=i+1
print(second_max)