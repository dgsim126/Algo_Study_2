'''
그냥 재귀로 풀라고 되어있네요
'''

def recursive(num, trial, current, depth):
    if(depth==trial):
        return current


    return recursive(num, trial, current*num, depth+1)

def solution(num, trial):
    return recursive(num, trial, 1, 0)


## main ##
T = 10
for test_case in range(1, T + 1):
    input()
    num, trial= map(int, input().split())
    print(f"#{test_case} {solution(num, trial)}")

# num= 2
# trial= 8
# print(solution(num, trial))