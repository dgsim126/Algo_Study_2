# 최대공약수를 구하자

def solution(a,b):
    if(a==b):
        return a

    big= max(a,b)
    small= min(a,b)

    if(small*2 == big):
        return small

    for i in range(big//2, 0, -1):
        # print(i)
        if(big%i==0 and small%i==0):
            return i

    return 1

## main ##
T = int(input())
for test_case in range(1, T + 1):
    a, b= map(int, input().split())
    print(f"#{test_case} {solution(a,b)}")
# a= 10
# b= 36
# print(solution(a,b))