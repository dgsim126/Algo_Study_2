'''
index=0에서 index=4까지 도착하는 것이 목표
현 위치에서 갈 수 있는 가장 멀리까지 먼저 가고 또 가장 멀리까지 가보는 방식
즉, dfs
'''

def solution(total, station):
    current_index= 0
    battery= station[0]

    global result
    result= 2147483647

    def dfs(current_index, battery, cnt):
        global result

        if(cnt>=result): # 가지치기
            return

        for i in range(battery, 0, -1):
            if(current_index+i>len(station)-1): # 탈출조건
                flag= True
                result= cnt
                return cnt+1
            new_index= current_index+i

            dfs(new_index, station[new_index], cnt+1)

    dfs(current_index, battery, 0)
    return result


## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    all= list(map(int, input().split()))
    print(f"#{test_case} {solution(all[0], all[1:])}")
# total= 10
# station= [2,1,3,2,2,5,4,2,1]
# print(solution(total, station))