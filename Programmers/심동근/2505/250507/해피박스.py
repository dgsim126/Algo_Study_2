'''
[상품번호, 상품크기, 상품가격, 우선순위(가격/크기)] 의 형태로 정리하여 리스트에 넣기
이때 우선순위는 크기가 클수록 우선순위를 가진다

그리디가 가능한가?
== 불가능. 예외 발생
== 또한, 그리디 문제였다면 N, M의 사이즈가 훨씬 컸을 듯

dfs 문제
dfs인 경우 [상품크기, 상품가격]만 있으면 될 듯(인덱스로 상품번호), is_used 필요
다음 depth로 넘어가면서 current_weight+=lst[i][0] && current_price++lst[i][1]
depth가 M에 도달하거나 current_weight가 N에 도달하면 갱신
'''

# def solution(N, M, lst):
#
#     def dfs(lst, is_used, current_weight, current_price, depth, N, M):
#         global result
#
#         # 탈출조건
#         if(depth==M):
#             if(result<current_price):
#                 result= current_price
#             return
#
#         for i in range(M):
#             if(is_used[i]==False):
#                 if(current_weight+lst[i][0]<=N):
#                     is_used[i]= True
#
#                     dfs(lst, is_used, current_weight+lst[i][0], current_price+lst[i][1], depth+1, N, M)
#
#                     is_used[i]= False
#                 else:
#                     if (result<current_price):
#                         result= current_price
#
#     global result
#     result= -1
#     is_used= [False]*M
#     current_weight= 0
#     current_price= 0
#
#     dfs(lst, is_used, current_weight, current_price, 1, N, M)
#
#     return result

# def solution(N, M, items):
#     dp = [0] * (N + 1)
#     print(dp)
#
#     for size, price in items:
#         for i in range(N, size - 1, -1):
#             dp[i] = max(dp[i], dp[i - size] + price)
#
#     return max(dp)

def solution(N, M, items):
    dp = [0] * (N + 1)
    print(f"초기 dp: {dp}\n")

    for idx, (size, price) in enumerate(items, 1):
        print(f"상품 {idx}: 크기={size}, 가격={price}")
        for i in range(N, size - 1, -1):
            old = dp[i]
            new = max(dp[i], dp[i - size] + price)
            dp[i] = new
            if old != new:
                print(f"  -> dp[{i}] 업데이트: max({old}, dp[{i - size}]({dp[i - size]}) + {price}) = {new}")
        print(f"  현재 dp 상태: {dp}\n")

    print(f"최종 dp: {dp}")
    return max(dp)


## main ##
# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     N, M= map(int, input().split())
#     lst= []
#     for i in range(M):
#         temp= list(map(int, input().split()))
#         lst.append(temp)
#
#     print(f"#{test_case} {solution(N, M, lst)}")

N= 10
M= 4
lst= [[6,12],[5,10],[5,15],[4,6]]
print(solution(N, M, lst))