'''
단순 구현?
- 제한시간 초과 발생 (1개 실패)
'''

def solution(N, M, lst):
    result= lst[0][:]

    for i in range(1, len(lst)):
        first_alpa= lst[i][0]
        flag= False

        for j in range(len(result)):
            if(result[j]>first_alpa):
                # new_result= result[0:j] + lst[i] + result[j:]
                # result= new_result[:]
                result[j:j] = lst[i]  # 리스트 중간 삽입(gpt)
                flag= True
                break

        if(flag==False):
            # new_result= result+lst[i]
            # result= new_result[:]
            result.extend(lst[i]) # 리스트 맨 뒤 삽입(gpt)

    return result[-1:-11:-1]


## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M= map(int, input().split())
    lst= []
    for i in range(N):
        lst.append(list(map(int, input().split())))
    print(f"#{test_case}", *solution(N, M, lst))
# N= 4
# M= 4
# lst= [[2,2,2,2],
# [3,3,3,3],
# [9, 10, 15, 116],
# [100,100,100,100]]
# print(solution(N, M, lst))