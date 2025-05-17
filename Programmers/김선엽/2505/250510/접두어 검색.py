def solution(N, M, stringA, stringB):
    answer = 0
    dicA = {}
    for i in range(N):
        # print(stringA[i][0], stringA[i])
        if stringA[i][0] not in dicA:
            dicA[stringA[i][0]] = [stringA[i]]
        else:
            dicA[stringA[i][0]].append(stringA[i])

    for i in range(M):
        if stringB[i][0] in dicA:
            array_a = dicA[stringB[i][0]]
            # print(array_a)
            for j in range(len(array_a)):
                is_pre = True
                if len(array_a[j]) >= len(stringB[i]):
                    for k in range(len(stringB[i])):
                        if stringB[i][k] != array_a[j][k]:
                            is_pre = False
                            break
                else:
                    continue
                if is_pre:
                    answer += 1
                    break
                else:
                    continue
        else:
            continue

    return answer

T = int(input())
for test_case in range(1, T+1):
    stringA = []
    stringB = []
    N, M = map(int, input().split())
    for _ in range(N):
        stringA.append(input())
    for _ in range(M):
        stringB.append(input())
    answer = solution(N, M, stringA, stringB)
    print(f"#{test_case} {answer}")