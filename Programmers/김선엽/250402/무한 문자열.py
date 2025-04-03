def solution(S, T):
    len_s = len(S)
    len_t = len(T)

    i_s = 0
    i_t = 0

    if S[i_s] != T[i_t]:
        return False

    while True:
        i_s += 1
        i_t += 1

        if i_s == len_s - 1 and i_t == len_t - 1:
            if S[i_s] != T[i_t]:
                return False
            return True

        if i_s >= len_s:
            i_s = 0
        if i_t >= len_t:
            i_t = 0

        if S[i_s] != T[i_t]:
            return False
        
T = int(input())
for test_case in range(1, T + 1):
    S, T = map(str, input().split())
    if solution(S, T):
        print(f"#{test_case} yes")
    else:
        print(f"#{test_case} no")