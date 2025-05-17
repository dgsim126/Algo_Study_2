'''
1. 부분 문자열 모두 구하기
permutation으로 구해야 하나? -> x 중간에 있는 글자가 빠져서는 안됨
그냥 for문으로 해야할 듯

-- 런타임 에러 발생(왜 안되는거야?)
'''

def solution(k, s):
    lst= set()
    # temp= []

    for start in range(len(s)):
        for end in range(start+1, len(s)+1):
            lst.add(s[start:end])
            # temp.append(s[start:end])

    # print(temp)
    lst= list(lst)


    result= sorted(lst)

    return result[k-1][0], len(result[k-1])

## main ##
# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     k, s= input().split()
#     print(f"#{test_case}", *solution(int(k), s))
k= 9
s= "ltsodjxzyc"
print(solution(k, s))