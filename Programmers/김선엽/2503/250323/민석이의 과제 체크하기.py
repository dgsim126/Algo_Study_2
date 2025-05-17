# def solution(num, submit, submit_list):
#     not_submit = set([i+1 for i in range(num)])
#     for i in range(submit):
#         not_submit.remove(submit_list[i])
    
#     not_submit = sorted(list(not_submit))

#     return not_submit

# print(solution(5, 3, [2,5,3]))

def solution(num, submit, submit_list):
    not_submit = set([i+1 for i in range(num)])
    for i in range(submit):
        not_submit.remove(submit_list[i])
    
    not_submit = sorted(list(not_submit))

    return not_submit

T = int(input())
for test_case in range(1, T+1):
    num, submit = map(int, input().split())
    submit_list = list(map(int, input().split()))
    answer = solution(num, submit, submit_list)
    
    print(f"#{test_case}", *answer)