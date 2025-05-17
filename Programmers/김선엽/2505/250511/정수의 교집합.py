def solution(N, M, list_A, list_B):
    answer = 0
    list_A = set(list_A)
    for i in range(M):
        if list_B[i] in list_A:
            answer += 1

    return answer

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    list_A = list(map(int, input().split()))
    list_B = list(map(int, input().split()))
    answer = solution(N, M, list_A, list_B)
    print(f"#{test_case} {answer}")