def convertToTen(N, word): # 16진수를 10진수로
    word= list(word)
    result= 0
    add_= 1
    for i in range(len(word)-1, -1, -1):
        if(word[i]=="A"):
            result+=(10*add_)
        elif(word[i]=="B"):
            result+=(11*add_)
        elif(word[i]=="C"):
            result+=(12*add_)
        elif(word[i]=="D"):
            result+=(13*add_)
        elif(word[i]=="E"):
            result+=(14*add_)
        elif(word[i]=="F"):
            result+=(15*add_)
        else:
            result+=(int(word[i])*add_)
        add_*=16

    return result

def convertToTwo(ten): # 10진수를 2진수로
    if(ten==0):
        return "0"
    elif(ten==1):
        return "01"
    elif(ten==2):
        return "010"
    elif(ten==3):
        return "011"

    result= ""
    while(ten>=2):
        result+=(str(ten%2))
        ten= ten//2
    result+="10"

    new_result= ""
    for i in range(len(result)-1, -1, -1):
        new_result+=result[i]

    return new_result

def solution(N, word):
    ten= convertToTen(N, word)
    two= convertToTwo(ten)
    return two

## main ##
T = int(input())
for test_case in range(1, T + 1):
    N, word= input().split()
    N= int(N)
    print(f"#{test_case} {solution(N, word)}")

