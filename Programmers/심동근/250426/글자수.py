
def solution(str1, str2):
    dic= {}

    for val in str1:
        dic[val]= 0

    for val in str2:
        if(val in dic.keys()):
            dic[val]+=1

    result= 0
    for key, value in dic.items():
        if(value>result):
            result= value

    return result

## main ##
T = int(input())
for test_case in range(1, T + 1):
    str1= list(input())
    str2= list(input())
    print(f"#{test_case} {solution(str1, str2)}")