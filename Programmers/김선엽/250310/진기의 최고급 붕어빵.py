# from collections import deque

# def solution(production, person):
#     N, M, K = production
#     end = person[-1]
#     wait_list = []
#     for i in range(M, end + 1, M):
#         wait_list.append([i, K])
    
#     wait_list = wait_list[::-1]

#     queue = deque(wait_list)

#     if not queue:   # 예외처리: 가장 마지막에 오는 사람도 빵이 만들어지기 전에 올 경우
#         return False

#     for i in range(N):
#         time, quantity = queue.pop()
#         if person[i] <= time:
#             return False
#         else:
#             quantity -= 1
#             if quantity > 0:
#                 queue.append([time, quantity])

#     return True


# if solution([2,2,2],[1,2]):
#     print("POSSIBLE")
# else:
#     print("IMPOSSIBLE")

### 테스트 케이스
### 1. 
### prodcution = [2, 2, 1], person = [3, 2] => for loop 종료 지점을 넉넉하기 잡아야 함
###
### 2.
### prodcution = [2, 2, 2], person = [1, 2] => 마지막 사람, person[-1]이 M과 같아 for loop이 안돌아 deque가 비어있는 경우
###
### 3.
### prodcution = [2, 2, 2], person = [4, 2] => person이 정렬이 안되어있는 경우

from collections import deque

T = int(input())
def solution(production, person):
    N, M, K = production
    end = person[-1]
    wait_list = []
    for i in range(M, end + 1 + M, M):
        wait_list.append([i, K])

    wait_list = wait_list[::-1]

    queue = deque(wait_list)

    if not queue:   # 예외처리: 가장 마지막에 오는 사람도 빵이 만들어지기 전에 올 경우
        return False

    for i in range(N):
        time, quantity = queue.pop()
        if person[i] < time:
            return False
        else:
            quantity -= 1
            if quantity > 0:
                queue.append([time, quantity])

    return True
    
for test_case in range(1, T + 1):
    production = list(map(int, input().split()))
    person = list(map(int, input().split()))

    person = sorted(person)

    if solution(production, person):
        print(f"#{test_case} Possible")
    else:
        print(f"#{test_case} Impossible")