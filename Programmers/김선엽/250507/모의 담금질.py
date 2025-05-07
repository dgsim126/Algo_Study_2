# from random import random
# import math
#
# def solution(T, T_end, k):
#     cost_pre = 100000
#     while T > T_end:
#         cost_new = cost()
#         diff = cost_new – cost_prev
#         if diff < 0 or math.exp(-diff / T) > random.random():
#             cost_pre = cost_new
#         T = T * k
#
# T = int(input())
# for test_case in range(1, T+1):
#     T, T_end, k = map(str, input().split())
#     answer = solution(T, T_end, k)
#     print(f"#{test_case} {answer}")