
# from collections import deque
#
# def solution(N, lst):
#     lst= deque(lst)
#
#     ## 왼쪽
#     temp= 0
#     i= 0
#     while(lst):
#         if(lst[i]>0):
#             temp+=lst[i]
#             i+=1
#         else:
#             if(abs(lst[i])>=temp):
#                 for i in range(i):
#                     lst.popleft()
#                 if(lst):
#                     lst.popleft()
#             break
#     while(lst):
#         if(lst[0]<0):
#             lst.popleft()
#         else:
#             break
#
#     # print(lst)
#     lst= deque(list(reversed(lst)))
#     # print(lst)
#
#     # 오른쪽
#     temp = 0
#     i = 0
#     while(lst):
#         if(lst[i] > 0):
#             temp+=lst[i]
#             i+=1
#         else:
#             if(abs(lst[i]) >= temp):
#                 for i in range(i):
#                     lst.popleft()
#                 if(lst):
#                     lst.popleft()
#             break
#     while(lst):
#         if (lst[0] < 0):
#             lst.popleft()
#         else:
#             break
#
#     print(lst)
#     lst= list(lst)
#
#
#     result= []
#     for i in range(0, len(lst)-1):
#         for j in range(i+1, len(lst)):
#             result.append(sum(lst[i:j+1]))
#
#     return max(result)
def solution(N, lst):
    result= []
    for i in range(0, len(lst) - 1):
        for j in range(i, len(lst)):
            result.append(sum(lst[i:j+1]))

    return max(result)



## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N= int(input())
    lst= list(map(int, input().split()))
    print(f"#{test_case} {solution(N, lst)}")
# N= 5
# lst= [1, 3, -8, 18, -8]
# print(solution(N, lst))