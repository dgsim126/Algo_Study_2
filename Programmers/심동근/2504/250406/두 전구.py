def solution(A, B, C, D):
    start = max(A, C)
    end = min(B, D)

    return max(0, end - start)

## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    A,B,C,D= map(int, input().split())
    print(f"#{test_case} {solution(A, B, C, D)}")

# A = 0
# B = 5
# C = 5
# D = 6
# print(solution(A, B, C, D))
