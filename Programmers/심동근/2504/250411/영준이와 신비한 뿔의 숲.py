'''
뿔 두개있는 동물을 a, 하나있는 동물을 b라고 한다면
2a+1b=n
2(a)+1(m-a)=n
2a+m-a=n
a=n-m
'''

def solution(n, m):
    return [m-(n-m), n-m]

## main ##
T = int(input())
for test_case in range(1, T + 1):
    n, m= map(int, input().split())
    print(f"#{test_case}" , *solution(n,m))
