T = int(input())
for test_case in range(1, T + 1):
    serv = list(map(int, input().split()))
    serv.sort()
    answer = 0

    # for i in range(serv[-1]+1, 1001):
    #     if (sum(serv) + i) % 7 == 0:
    #         answer = i
    #         break

    i = serv[-1]+1
    while True:
        if (sum(serv) + i) % 7 == 0:
            answer = i
            break
        i += 1

    print(answer)