

def solution(a, b, c):
    if(a==b==c):
        return a
    if(a==b):
        return c
    if(a==c):
        return b
    if(b==c):
        return a


## main ##
T = int(input())
for test_case in range(1, T + 1):
    a, b, c= map(int, input().split())
    print(f"#{test_case} {solution(a, b, c)}")