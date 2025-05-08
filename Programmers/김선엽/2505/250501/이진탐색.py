def solution(P, I):
    answer = 0
    start = 1
    end = P
    while P != I:
        answer += 1
        P = int((start + end)/2)
        if P > I:
            end = P
        elif P < I:
            start = P
        else:
            break

    return answer

T = int(input())
for test_case in range(1, T+1):
    P, A, B = map(int, input().split())
    answer1 = solution(P, A)
    answer2 = solution(P, B)
    if answer1 > answer2:
        print(f"#{test_case} B")
    elif answer1 == answer2:
        print(f"#{test_case} 0")
    else:
        print(f"#{test_case} A")