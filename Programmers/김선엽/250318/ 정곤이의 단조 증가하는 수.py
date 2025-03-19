from itertools import combinations

def solution(numbers):
    num_set = set()
    for comb in combinations(numbers, 2):
        nums_ = comb[0] * comb[1]
        str_nums = str(nums_)
        possible = True
        for i in range(len(str_nums)-1):
            if str_nums[i] > str_nums[i+1]:
                possible = False
                break
        if possible:
            num_set.add(nums_)
    
    if num_set:
        return max(num_set)
    else:
        return -1

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    numbers = list(map(int, input().split()))
    answer = solution(numbers)

    print(f"#{test_case} {answer}")