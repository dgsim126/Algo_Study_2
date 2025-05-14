from collections import deque


def solution(N, M, temp):
    pizza= []
    for i in range(M):
        pizza.append([i+1, temp[i]])

    oven= pizza[:N]
    oven= deque(oven)
    pizza= pizza[N:]
    pizza= deque(pizza)

    while(oven):
        if(len(oven)==1):
            return oven[0][0]
        index, cheese= oven.popleft()

        cheese//=2
        if(cheese in [1, 0]): # 맨 앞 피자가 다 녹은 경우
            # 아직 오븐에 넣지 않은 피자가 있을 때
            if(pizza):
                oven.append(pizza.popleft())
        else:
            oven.append((index, cheese))


## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M= map(int, input().split())
    pizza= list(map(int, input().split()))
    print(f"#{test_case} {solution(N, M, pizza)}")
# N= 3
# M= 5
# pizza= [7,2,6,5,3]
# print(solution(N, M, pizza))