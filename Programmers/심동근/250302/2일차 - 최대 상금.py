'''
price를 change만큼 변경 가능

그리디로 생각하면 될 듯. 가장 맨 앞의 숫자와 그 외 숫자 중 가장 큰 수를 찾아 위치를 교환하는 방식(그 외 숫자 중 가장 큰 숫자는 인덱스 뒤부터)
-> 그리디로 풀면 안될 듯. 숫자가 내림차순 정렬인 경우 문제 발생. 또한 동일한 위치의 교환이 가능하다는 점

완전탐색으로 도전해야할 듯. 최대자리수가 6자리이게 때문에 완전탐색을 수행해도 가능할 것으로 추측
- dfs로 하려 했는데 생각해보니 순열 사용하면 될 듯
- 순열을 사용한 후, 각 순열을 가져와 기존값과 달라진 부분이 몇 개인지 파악하면 될 듯

'''
from itertools import permutations


def solution(price, change):
    len_= len(str(price))
    price= list(str(price))
    lst= list(permutations(price, len_))
    result= []

    for i in range(len(lst)):
        cnt= 0
        for j in range(len_):
            if(price[j]!=lst[i][j]):
                cnt+=1
        if(cnt==change*2):
            result.append(int("".join(lst[i])))

    result= sorted(result, reverse=True)

    return result[0]



## main ##
price= 32888
change= 1
print(solution(price, change))

# =====================================================================================================================
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
