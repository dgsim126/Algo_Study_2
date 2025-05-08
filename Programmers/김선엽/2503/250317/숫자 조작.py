# ## 왤케 어렵지?ㅋㅋ
# Min에서 0처리를 안해줬음..........

# def findMax(num):
#     if num == 0:
#         return 0
    
#     num_list = list(str(num))
#     i = 0
#     while i < len(num_list):
#         cur = int(num_list[i])
#         max = 0
#         max_i = 0

#         for index in range(i+1, len(num_list)):
#             if int(num_list[index]) >= max:
#                 max = int(num_list[index])
#                 max_i = index
        
#         if max > cur:
#             num_list[i], num_list[max_i] = num_list[max_i], num_list[i]
#             break
#         else:
#             i += 1
    
#     return int("".join(num_list))

# def findMin(num):
#     if num == 0:
#         return 0
    
#     num_list = list(str(num))
#     i = 0
#     while i < len(num_list):
#         cur = int(num_list[i])
#         min = 10
#         min_i = 0

#         for index in range(i+1, len(num_list)):
#             if int(num_list[index]) < min:
#                 min = int(num_list[index])
#                 min_i = index
        
#         if min < cur:
#             num_list[i], num_list[min_i] = num_list[min_i], num_list[i]
#             break
#         else:
#             i += 1
    
#     return int("".join(num_list))

# max = findMax(142857)
# min = findMin(142857)
# print(f"#1 {min} {max}")



## 제출

def findMax(num):
    if num == 0:
        return 0
    
    num_list = list(str(num))
    i = 0
    while i < len(num_list):
        cur = int(num_list[i])
        max = 0
        max_i = 0

        for index in range(i+1, len(num_list)):
            if int(num_list[index]) >= max:
                max = int(num_list[index])
                max_i = index
        
        if max > cur:
            num_list[i], num_list[max_i] = num_list[max_i], num_list[i]
            break
        else:
            i += 1
    
    return int("".join(num_list))

def findMin(num):
    if num == 0:
        return 0
    
    num_list = list(str(num))
    i = 0
    while i < len(num_list) - 1:
        cur = int(num_list[i])

        if cur == 0:
            i += 1
            continue
        min = 10
        min_i = 0

        for index in range(i+1, len(num_list)):
            if i == 0:
                if int(num_list[index]) < min and int(num_list[index]) != 0:
                    min = int(num_list[index])
                    min_i = index
            else:
                if int(num_list[index]) < min:
                    min = int(num_list[index])
                    min_i = index
        
        if min < cur:
            num_list[i], num_list[min_i] = num_list[min_i], num_list[i]
            break
        else:
            i += 1
    
    return int("".join(num_list))

T = int(input())
for test_case in range(1, T+1):
    num = int(input())
    max = findMax(num)
    min = findMin(num)
    
    print(f"#{test_case} {min} {max}")