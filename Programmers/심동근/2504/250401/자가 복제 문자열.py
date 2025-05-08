'''
제한시간 초과 발생
K의 범위가 10^18이기에 발생한 문제같음
-- 지금 이 방법이 안된다면 수학을 통해 직접 할당하지 않고 계산해야할 것 같음
역으로 생각해보자 예를 들어 k=7인 경우
포기

'''
import time

def change(num):
    result= ""

    for i in range(len(num)):
        if(num[i]=="0"):
            result+="1"
        else:
            result+="0"

    answer= ""
    for i in range(len(result)-1, -1, -1):
        answer+=result[i]

    return answer

def solution(K, P):
    i= "0"

    while(True):
        if(K<=len(i)):
            # print(i)
            return i[K-1]
        i= i+"0"+change(i)


## main ##
# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     K= int(input())
#     P= 0
#     print(f"#{test_case} {solution(K,P)}")
K= 3
P= 0
print(solution(K, P))

