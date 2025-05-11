

def is_prime(val):
    if val in [1,4,6]:
        return False
    if val in [2,3,5]:
        return True
    if(val%2==0):
        return False

    # print(val, int(val**(1/2))+1)
    for i in range(3, int(val**(1/2))+1, 2):
        if(val%i==0):
            # print("val%i", val, i)
            return False

    return True

def solution(a, b):
    result= 0

    for i in range(a+1, b):
        if(is_prime(i)==True):
            # print(i)
            result+=i

    return result

## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a, b= map(int, input().split())
    print(f"#{test_case} {solution(a, b)}")
# a= 5
# b= 23
# print(solution(a, b))