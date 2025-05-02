def recursive(N, M, depth):
    if(depth==M):
        return N

    return N*recursive(N, M, depth+1)

def solution(N, M):

    return recursive(N, M, 1)

## main ##
T = 10
for test_case in range(1, T + 1):
    input()
    num, trial= map(int, input().split())
    print(f"#{test_case} {solution(num, trial)}")
# N= 9
# M= 8
# print(solution(N, M))