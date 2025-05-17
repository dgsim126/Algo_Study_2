def solution(N, bus, P, P_list):
    num_dic = {}
    for i in range(1, 5001):
        num_dic[i] = 0
    
    for i in range(N):
        for j in range(bus[i][0], bus[i][1] + 1):
            num_dic[j] += 1

    answer = []

    for i in range(P):
        answer.append(num_dic[P_list[i]])
    
    return answer

T = int(input())
for test_case in range(1, T+1):
    bus = []
    P_list = []
    N = int(input())
    for _ in range(N):
        bus.append(list(map(int, input().split())))
    
    P = int(input())

    for _ in range(P):
        P_list.append(int(input()))

    answer = solution(N, bus, P, P_list)

    print(f"#{test_case}", *answer)