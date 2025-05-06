# import sys
# sys.stdin = open("data/input (9).txt", "r")

def solution(password):
    # print(password)
    num_dic = {"3211": 0, "2221": 1, "2122": 2, "1411": 3, "1132": 4, "1231": 5, "1114": 6, "1312": 7, "1213": 8, "3112": 9}
    key = []
    for i in range(0, 56, 7):
        cur = ""
        count = 0
        for j in range(i, i+7):
            # print(cur)
            if j == i + 6:
                if password[j] == password[j - 1]:
                    cur += str(count+1)
                else:
                    cur += str(count)
                    cur += "1"
            else:
                if count == 0:
                    count += 1
                else:
                    if password[j] == password[j-1]:
                        count += 1
                    else:
                        cur += str(count)
                        count = 1
        # print(cur)
        key.append(num_dic[cur])
    # print(key)
    odd = 0
    even = 0
    for i in range(8):
        if i % 2 == 0:
            odd += key[i]
        else:
            even += key[i]

    if (odd * 3 + even) == 0:
        return 0
    else:
        if (odd * 3 + even) % 10 == 0:
            return sum(key)
        else:
            return 0

T = int(input())
for test_case in range(1, T+1):
    N = int(input()[0:2])
    # print(N)
    # N, M = 10, 70
    for _ in range(N):
        container = list(input())
        if "1" in container:
            for i in range(len(container)-1, -1, -1):
                if container[i] == "1":
                    password = container[i-55:i+1]
                    break
    answer = solution(password)
    print(f"#{test_case} {answer}")