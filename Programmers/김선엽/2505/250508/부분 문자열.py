## N 번째 첫 글자와 글자 수

def solution(N, strings):
    num_dic = {}
    for i in range(len(strings)):
        if strings[i] not in num_dic:
            num_dic[strings[i]] = [strings[i:]]
        else:
            num_dic[strings[i]].append(strings[i:])

    num_dic = dict(sorted(num_dic.items(), key=lambda x: x[0]))

    for key, value in num_dic.items():
        value = sorted(value)
        # print(value)
        for i in range(len(value)):
            if i == 0:
                if N <= len(value[i]):
                    # print("here")
                    return [value[i][0], N]
                else:
                    # print("there")
                    N -= len(value[i])
            else:
                count = 0   ## 앞 부분과 겹치는 부분수열 제외
                if len(value[i-1]) <= len(value[i]):
                    for j in range(len(value[i-1])):
                        if value[i][j] == value[i-1][j]:
                            count += 1
                        else:
                            break
                else:
                    for j in range(len(value[i])):
                        if value[i][j] == value[i-1][j]:
                            count += 1
                        else:
                            break
                # print(count)
                if N <= len(value[i]) - count:
                    return [value[i][0], N + count]
                else:
                    N -= (len(value[i]) - count)

T = int(input())
for test_case in range(1, T+1):
    N, strings = map(str, input().split())
    answer = solution(int(N), strings)
    print(f"#{test_case}", *answer)