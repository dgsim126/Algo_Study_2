'''
11일 11시 11분을 분 단위로 변경, 입력받은 시간도 분으로 변경 후 비교
'''

def solution(D, H, M):
    start_time= 11 + (60*11) + (11*60*24)
    end_time= M + (H*60) + (D*60*24)

    if(start_time>end_time):
        return -1
    return end_time-start_time

## main ##
T = int(input())
for test_case in range(1, T + 1):
    D, H, M= map(int, input().split())
    print(f"#{test_case} {solution(D, H, M)}")

# D= 11
# H= 3
# M= 7
# print(solution(D, H, M))