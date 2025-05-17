def solution(N, M, origin, extend_):
    for extend_ in extends_:
        # print(origin)
        is_exist = False
        k = extend_[0]
        for i in range(len(origin)):
            if k < origin[i]:
                origin[i:i] = extend_
                is_exist = True
                break
        if not is_exist:
            origin = origin + extend_

    # print(origin)

    if len(origin) < 10:
        return origin[::-1]
    else:
        return origin[-1:-11:-1]

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    origin = list(map(int, input().split()))
    extends_ = []
    for _ in range(M-1):
        extends_.append(list(map(int, input().split())))
    answer = solution(N, M, origin, extends_)
    # print(answer)
    print(f"#{test_case}", *answer)