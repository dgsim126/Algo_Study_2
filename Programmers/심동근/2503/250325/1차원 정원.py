def solution(N, D):
    water= (D*2)+1

    if(N%water==0):
        return N//water
    else:
        return N//water + 1

## main ##
T = int(input())
for test_case in range(1, T + 1):
    N, D= map(int, input().split())
    print(f"#{test_case} {solution(N, D)}")