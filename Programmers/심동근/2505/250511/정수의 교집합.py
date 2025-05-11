'''
둘 다 set으로 바꾼다

'''
def solution(N_list, M_list):
    N_list= set(N_list)
    M_list= set(M_list)

    big= len(N_list)+len(M_list)
    small= len(N_list.union(M_list))

    return big-small


## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M= map(int, input().split())
    N_list= list(map(int, input().split()))
    M_list= list(map(int, input().split()))
    print(f"#{test_case} {solution(N_list, M_list)}")

# N= 4
# M= 5
# N_list= [1,3,5, 6]
# M_list= [2,4,6,8,10]
# print(solution(N, M, N_list, M_list))