'''
문제가 너무 쉽다!
<= 해당 조건만 잘 보면 엣지 케이스 없음
'''

def solution(min_time, max_time, current_time):

    if(current_time<min_time):
        return min_time-current_time
    elif(current_time<=max_time):
        return 0
    else:
        return -1



## main ##
T = int(input())
for test_case in range(1, T + 1):
    L, U, X= map(int, input().split())
    print(f"#{test_case} {solution(L, U, X)}")
# L= 300 # L분 이상
# U= 300 # U분 이상
# X= 300 # 현재 운동한 시간
# print(solution(L, U, X))