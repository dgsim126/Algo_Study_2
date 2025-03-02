'''
현재 내 위치를 기준으로 리스트의 -2 ~ +2 영역을 탐색하여 가장 큰 값을 찾는다.
찾은 가장 큰 값과 본인의 값을 비교하여 (본인의 값) - (가장 큰 값) 을 계산하여 결과에 더한다.
'''

def solution(N, buildings):
    result= 0

    for i in range(N):
        if(i<=1):
            lst= buildings[0:i]+buildings[i+1:i+3]
        elif(i>=N-2):
            lst= buildings[i-2:i]+buildings[i+1:N]
        elif(1<i and i<N-2):
            lst= buildings[i-2:i]+buildings[i+1:i+3]
        else:
            print("impossible")

        max_val= max(lst)
        current_val= buildings[i]

        if(current_val>max_val):
            result+=(current_val-max_val)

    return result



## main ##
for test_case in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    result= solution(N, buildings)
    print(f'#{test_case} {result}')



