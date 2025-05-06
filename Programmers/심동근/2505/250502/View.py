'''
현 위치 인덱스와
주변 인덱스 4개의 최댓값을 계속 비교
'''

def solution(N, lst):
    lst= [0,0]+lst+[0,0]
    result= 0

    for i in range(2, N+2):
        current= lst[i]
        side_max= max(lst[i-2], lst[i-1], lst[i+1], lst[i+2])

        if(current>side_max):
            result+= (current-side_max)

    return result


## main ##
for test_case in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    result= solution(N, buildings)
    print(f'#{test_case} {result}')

# N= 10
# lst= [0, 0, 254, 185, 76, 227, 84, 175, 0, 0]
# print(solution(N, lst))