def solution(lights):
    l_list = [[lights[0], lights[1]], [lights[2], lights[3]]]
    l_list = sorted(l_list, key=lambda x: x[0])

    A, B = l_list[0]
    C, D = l_list[1]

    if B <= C:
        return 0
    else:
        if D <= B:
            return D - C
        else:
            return B - C

T = int(input())
for test_case in range(1, T+1):
    lights = list(map(int, input().split()))
    answer = solution(lights)

    print(f"#{test_case} {answer}")