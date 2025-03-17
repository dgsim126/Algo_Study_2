# # 풀이

# from itertools import combinations

# def solution(numbers):
#     num_set = set()
#     for comb in combinations(numbers, 3):
#         num_set.add(sum(comb))

#     for i in range(4):
#         num_set.remove(max(num_set))
    
#     return max(num_set)


# numbers = list(map(int, input().split()))
# print(solution(numbers))


from itertools import combinations

def solution(numbers):
    num_set = set()
    for comb in combinations(numbers, 3):
        num_set.add(sum(comb))
    max_list = sorted(num_set, reverse=True)
    return max_list[4]

T = int(input())
for test_case in range(1, T + 1):
    numbers = list(map(int, input().split()))
    answer = solution(numbers)
    print(f"#{test_case} {answer}")