# T = int(input())
# for test_case in range(1, T + 1):
#     num = int(input())
#     if num ** 0.5 == int(num ** 0.5):
#         print(f'#{test_case} 1')
#     else:
#         for i in range(1, 10000000):
#             if (num * i) ** 0.5 == int((num * i) ** 0.5):
#                 print(f'#{test_case} {i}')
#                 break

# 이건 더한 결과가 제곱이 되는 최소 자연수
# T = int(input())
# for test_case in range(1, T + 1):
#     num = int(input())
#     if num ** 0.5 == int(num ** 0.5):
#         print(f'#{test_case} 1')
#     else:
#         nxt = int(num ** 0.5)
#         while True:
#             nxt_num = nxt**2
#             if nxt_num > num:
#                 print(f'#{test_case} {nxt_num-num}')
#                 break
#             nxt += 1

T = int(input())
for test_case in range(1, T + 1):
    num = int(input())
    if num ** 0.5 == int(num ** 0.5):
        print(f'#{test_case} 1')
    else:
        nxt = int(num ** 0.5)+1
        while True:
            nxt_num = nxt**2
            if nxt_num % num == 0:
                print(f'#{test_case} {nxt_num // num}')
                break
            nxt += 1