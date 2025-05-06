def solution(str1, str2):
    if(str1 in str2):
        return 1
    else:
        return 0

## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str1= input()
    str2= input()
    print(f"#{test_case} {solution(str1, str2)}")

# str1= "XYPV"
# str2= "EOGGXYPVSY"
# print(solution(str1, str2))
