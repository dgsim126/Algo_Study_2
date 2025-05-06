from itertools import combinations

def solution(a, b):
    legnth = 0
    
    if len(a) >= len(b):
        length = len(b)
        list1 = b
        list2 = a
    else:
        length = len(a)
        list1 = a
        list2 = b

    for i in range(length, 0, -1):
        s = set([comb1 for comb1 in combinations(list1, i)])
        for comb2 in combinations(list2, i):
            if comb2 in s:
                return i
            
    return 0

T = int(input())
for test_case in range(1, T+1):
    a, b = map(str, input().split())
    answer = solution(a, b)

    print(f"#{test_case} {answer}")