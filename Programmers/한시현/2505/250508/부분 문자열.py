# 런타임 에러
T = int(input())
for test_case in range(1, T + 1):
    n, s = input().split()
    int_n = int(n)

    subs = []
    len_s = len(s)

    for i in range(len_s):
        for j in range(i + 1, len_s + 1):
            subs.append(s[i:j])

    subs = list(set(subs))
    subs.sort() # set()과 순서 조심
    target = subs[int_n - 1]

    print(f"#{test_case} {target[0]} {len(target)}")