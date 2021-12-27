binary_number = [1, 0, 0, 1, 1, 0, 1, 1]
i=1
power=0
sum=0
while i<=len(binary_number):
    AS=(2**power)*binary_number[-i]
    power+=1
    sum+=AS
    i+=1
print(sum)    