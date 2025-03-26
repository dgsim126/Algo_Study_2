def solution(N, nums):
    num_dict = {
        "ZRO": 0,
        "ONE": 1,
        "TWO": 2,
        "THR": 3,
        "FOR": 4,
        "FIV": 5,
        "SIX": 6,
        "SVN": 7,
        "EGT": 8,
        "NIN": 9,
    }
    sort_list = []
    for i in range(len(nums)):
        sort_list.append([num_dict[nums[i]], i])
    
    sort_list = sorted(sort_list, key=lambda x: x[0])

    answer = []
    for i in sort_list:
        answer.append(nums[i[1]])
    
    return answer

# print(solution(6, ["SIX", "SVN", "ZRO", "NIN", "TWO", "TWO"]))

T = int(input())
for test_case in range(1, T+1):
    a, b = map(str, input().split())
    N = int(b)
    nums = list(map(str, input().split()))
    
    answer = solution(N, nums)

    print(f"#{test_case}")
    print(*answer)