'''
B에 있는 문자열이 A의 접두어인 경우
A의 모든 단어로 만들 수 있는 모든 접두어를 만든다.(set을 이용)
B가 A에 있는지 확인
'''

def solution(A, B):
    all= set()
    for i in range(len(A)):
        for j in range(1, len(A[i])+1):
            all.add(A[i][0:j])

    result= 0

    for i in B:
        if(i in all):
            result+=1

    return result

## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    A, B= map(int, input().split())
    A_list= []
    B_list= []
    for i in range(A):
        A_list.append(input())
    for i in range(B):
        B_list.append(input())
    print(f"#{test_case} {solution(A_list, B_list)}")
# A= 3
# B= 5
# A_list= ["people", "water", "night"]
# B_list= ["wa", "h", "country", "ni", "people"]
# print(solution(A_list, B_list))