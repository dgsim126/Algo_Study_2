def solution(N):
    if N > 10:
        return "0.00000" # <<<<<<<<<<<<<<
    deno = 9
    numer = 9
    start = 9
    for i in range(N-1):
        numer *= start
        start -= 1
        deno *= 10

    answer = numer / deno
    answer = round(answer, 5)
    answer = str(answer)

    if len(str(answer)) < 7:
        k = 7 - len(str(answer))
        add_str = "0" * k
        answer += add_str

    return answer
    # print(answer)

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    answer = solution(N)
    print(f"#{test_case} {answer}")