'''
가장 큰 수와 가장 작은 수를 찾아낸다.
- 인덱스가 가장 큰 가장 큰 수와 첫 번째 값을 바꾸면 가장 큰 수를 만들 수 있다!
- 인덱스가 가장 작은 수 중 인덱스가 가장 작은 값과 첫 번째 값을 바꾸면 가장 작은 수를 만들 수 있다.



왜 안되는지 도저히 모르겠음
'''

def solution(N):
    if(N==0):
        return [0, 0]
    lst= list(map(int, str((N))))
    max_value= max(lst)
    max_value_index= list(reversed(lst)).index(max_value)
    max_value_index= len(lst)-max_value_index-1
    # print(max_value, max_value_index, lst[max_value_index])

    temp_lst= []
    for i in range(len(lst)):
        if(lst[i]!=0):
            temp_lst.append(lst[i])

    min_value= min(temp_lst)
    min_value_index= lst.index(min_value)
    # print(min_value, min_value_index)

    # 가장 큰 값
    biggest= lst[:]
    temp= biggest[0]
    biggest[0]= biggest[max_value_index]
    biggest[max_value_index]= temp

    # 가장 작은 값
    smallest= lst[:]
    temp= smallest[0]
    smallest[0]= smallest[min_value_index]
    smallest[min_value_index]= temp

    return [int("".join(map(str, smallest))), int("".join(map(str, biggest)))]



## main ##
# T = int(input())
# for test_case in range(1, T + 1):
#     N= int(input())
#     result= solution(N)
#     print(f"#{test_case} {result[0]} {result[1]}")
N= 11110 # 11110 넣으면 [11110, 11110] 이런 결과가 나와버림(최소값 만족 실패)
print(solution(N))