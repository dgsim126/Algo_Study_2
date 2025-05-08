'''
로직 수정 필요
1. current_point를 생성(초기값 0)
2. current_point 뒤에 값들을 확인하여 가장 큰 값(max_val) 찾기
3. max_val의 인덱스 찾기(이때, lst의 뒤에서부터 우선하여 찾는다.)
4. 위치교환
4-1. 현재 current_point 뒤에 존재하는 값이 1개라면 current_point를 증가시키지 않는다.
     해당 경우는 반복문 중단 후, 남은 교체횟수가 짝수인지 홀수인지 확인하여 lst[-1], lst[-2]의 값을 교환
4-2. 현재 current_point 뒤에 존재하는 값이 2개 이상이라면 current_point를 증가시킨다.

문제발생
32888의 경우 3을 먼저 바꾸고 2를 바꾸는데
그렇게하면 88823이 정답이 된다. 2를 먼저 바꾸면 88832가 된다
- 이거까지 고려하면 경우의 수가 너무 많은데.. 접근방식이 잘못되었나?

'''

# def solution(num, times):
#     lst= list(str(num))
#     flag= False
#     current_index= 0
#
#     while(times>0):
#         max_val= max(lst[current_index+1:])
#         max_val_index= -1
#
#         for i in range(len(lst)-1, current_index, -1):
#             print(i)
#             if(lst[i]==max_val):
#                 max_val_index= i
#                 break
#         print(f"current lst= {lst}")
#         print(f"current_index= {current_index}, max_val= {max_val}, max_val_index= {max_val_index}")
#
#         temp= lst[current_index]
#         lst[current_index]= lst[max_val_index]
#         lst[max_val_index]= temp
#         print(f"after lst= {lst}")
#         print()
#
#         times-=1
#         current_index+=1
#
#         if(len(lst[current_index+1:])<2):
#             flag= True
#             break
#
#     if(flag==True and times%2==1):
#         temp= lst[-1]
#         lst[-1]= lst[-2]
#         lst[-2]= temp
#
#     return lst
#
# ## main ##
# num= 32888
# times= 2
# print(solution(num, times))


def solution(price, change):
    price = list(str(price))  # 숫자를 리스트로 변환
    max_value = [0]  # 최댓값을 저장할 변수 (mutable list)
    visited = set()  # 중복된 상태를 저장할 해시셋

    def dfs(depth, change_left):
        nonlocal max_value

        # 현재 상태를 문자열로 변환하여 중복 체크
        key = ("".join(price), change_left)
        if key in visited:
            return
        visited.add(key)  # 현재 상태를 저장

        # 교환 횟수를 모두 사용한 경우 최댓값 갱신
        if change_left == 0:
            max_value[0] = max(max_value[0], int("".join(price)))
            return

        # 현재 상태에서 가능한 모든 자리 교환 탐색
        for i in range(len(price)):
            for j in range(i + 1, len(price)):
                # 두 숫자를 교환
                price[i], price[j] = price[j], price[i]
                dfs(depth + 1, change_left - 1)  # 다음 단계 진행
                price[i], price[j] = price[j], price[i]  # 원상 복구 (백트래킹)

    dfs(0, change)  # DFS 실행
    return max_value[0]  # 최댓값 반환


## main ##
T = int(input())  # 테스트 케이스 개수

for test_case in range(1, T + 1):
    price, change = map(int, input().split())  # 가격과 교환 횟수 입력
    result = solution(price, change)
    print(f"#{test_case} {result}")