'''
yard에서 2개씩 확인하면 된다.
예외 (|)인 경우 조심 - 방지하기 위해 값을 계속 변경하는 방식으로 진행할 것:  이런 경우는 가정되지 않음
'''

def solution(yard):
    yard= list(yard)
    result= 0
    for i in range(len(yard)-1):
        current_area= yard[i:i+2]
        if(current_area==["(","|"]):
            result+=1
            yard[i+1]= ")"
        elif(current_area==["|",")"]):
            result+=1
            yard[i]= "("
        elif(current_area==["(",")"]):
            result+=1

    return result


## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    yard= input()
    print(f"#{test_case} {solution(yard)}")


# yard= ".|.(|...(|(|...().("
# print(solution(yard))