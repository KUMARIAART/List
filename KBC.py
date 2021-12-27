question_list = [
    "How many continents are there?", 
    "What is the capital of India?", 
    "NG mei kaun se course padhaya jaata hai?" 
]
options_list = [
    ["Four", "Nine", "Seven", "Eight"],
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]
solution_list = [3, 4, 1]
anser_list=[
    ["1.four","3.seven"],
    ["2.bhopal","4. delhi"],
    ["3.counseling","1.software engineering"]
]
i=0
a=0
k=1
count=0
while i<len(question_list):
    print(question_list[i])
    j=0
    s=1
    while j<len(options_list[i]):
        p=(options_list[i][j])
        print(j+1,p)
        j+=1
    lyflin=input("do u want lifeline:")
    if lyflin=="yes":
        print("50 50 lyfline")
        if count<1:
            print(anser_list[i])
            v=int(input("enter the answer:"))
            if v==solution_list[i]:
                s+=10000
                print("ur anser is correct")
                print("u win Rs/-",s)
            else:
                print("ur answr is incorrect")
                break
            count=count+1
        else:
            print("u have already used lifline")
            m=int(input("enter ur answer"))
            if m==solution_list[i]:
                print("congratrs,ur answer is right")
                s=s+1000
                print("u win Rs/-",s)
            else:
                print("ur answr is wrong")
                print("u can play again")
                print("u win ",s)
                break
    else:
        l=int(input("enter ur answr"))
        if l==solution_list[i]:
            print("right answr")
            s=s+10000
            print("u win Rs/-",s)
        else:
            print("no chance")

    i+=1
       
    
        

    

