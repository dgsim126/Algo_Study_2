'''
결론은 페르마의 소정리를 사용해서 풀어야 하는 문제
이런 문제 절대 안 나옴
'''

def solution(N, R): # 10, 2
    child= 1
    for i in range(N, N-R, -1):
        child*=i

    parent= 1
    for i in range(R, 0, -1):
        parent*=i

    return (child//parent)%1234567891


## main ##
# T = int(input())
# for test_case in range(1, T + 1):
#     N, R= input().split()
#     N= int(N)
#     R= int(R)
#     result= solution(N, R)
#     print(f"#{test_case} {result}")
print(solution(3,0))
