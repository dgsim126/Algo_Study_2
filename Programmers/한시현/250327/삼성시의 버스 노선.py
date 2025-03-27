T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    AB = []
    for _ in range(N):
        Ai, Bi = map(int, input().split())
        AB.append([Ai, Bi])
    P = int(input())
    Cj = []

    for _ in range(P):
        Cj.append(int(input()))

    covers = []
    for i in AB:
        ran = [n for n in range(i[0], i[1]+1)]
        covers.append(ran)

    answer = []
    for j in Cj:
        count = 0
        for cover in covers:
            if j in cover:
                count += 1
        answer.append(count)

    real_answer = ' '.join(map(str, answer))
    print(f'#{test_case} {real_answer}')