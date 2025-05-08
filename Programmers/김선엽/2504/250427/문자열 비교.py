def solution(str1, str2):
    len_s1 = len(str1)
    len_s2 = len(str2)

    for i in range(len_s2 + 1 - len_s1):
        if str2[i:i+len_s1] == str1:
            return 1
        
    return 0

T = int(input())
for test_case in range(1, T+1):
    str1 = input()
    str2 = input()
    answer = solution(str1, str2)

    print(f"#{test_case} {answer}")