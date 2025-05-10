'''
딕셔너리를 활용하여 풀어야 할 것 같음
'''

def solution(N, M, lst):

    def check(dic, key):
        global people

        if key not in dic.keys(): # 단일 팀
            return

        for value in dic[key]:
            if(people[value]==0):
                people[value]= 1
                check(dic, value)


    dic= {}
    global people
    people= [0]*(N+1) # 인덱스 0 제외
    result= 0

    for i in range(0, len(lst), 2):
        # print(i)
        key= lst[i]
        value= lst[i+1]

        if key in dic.keys():
            dic[key].append(value)
        else:
            dic[key]= [value]

        if value in dic:
            dic[value].append(key)
        else:
            dic[value] = [key]

    # print(dic)

    for i in range(1, N+1):
        if(people[i]==0):
            result+=1
            people[i]= 1
            check(dic, i)

    return result

## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M= map(int, input().split())
    lst= list(map(int, input().split()))
    print(f"#{test_case} {solution(N, M, lst)}")
# N= 5
# M= 3
# lst= [1,2,3,4,5,1]
# print(solution(N, M, lst))