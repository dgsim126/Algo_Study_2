# 백준 골드 1 난이도
# 페르마의 소정리, 분할 정복을 활용한 풀이

# def solution(comb):
#     N, R = comb
#     half = N // 2
#     if R > half:
#         R = N - R
    
#     demo = 1
#     numer = 1

#     length = R

#     for i in range(length):
#         demo *= N
#         N -= 1
#         numer *= R
#         R -= 1

#     return int(demo/numer)

# print(solution([10, 2]))

T = int(input())
for test_case in range(1, T + 1):
    comb = list(map(int, input().split()))
    N, R = comb
    MOD = 1234567891
    half = N // 2
    if R > half:
        R = N - R
        
    demo = 1
    numer = 1

    length = R

    for i in range(length):
        demo *= N
        N -= 1
        numer *= R
        R -= 1

    answer = int((demo/numer) % MOD)

    print(f"#{test_case} {answer}")