def solution(str1, str2):
    s_dic = {}
    for s1 in str1:
        if s1 not in s_dic:
            s_dic[s1] = 0
    
    for s2 in str2:
        if s2 in s_dic:
            s_dic[s2] += 1
    
    max = 0
    for value in s_dic.values():
        if value > max:
            max = value
    
    return max

T = int(input())
for test_case in range(1, T+1):
    str1 = input()
    str2 = input()
    answer = solution(str1, str2)

    print(f"#{test_case} {answer}")