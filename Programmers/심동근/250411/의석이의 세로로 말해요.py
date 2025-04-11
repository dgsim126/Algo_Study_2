

def solution(lst):
    result= ""

    for j in range(15): #[i][j]
        for i in range(5):
            if(len(lst[i])>j):
                # print(lst[i][j])
                result+=lst[i][j]
        # result+=" "

    return result

## main ##
#lst= [["A","B","C","D","E"],["a","b","c","d","e"],["0","1","3","4"],["F","G","H","I","J"],["f","g","h","i","j"]]
# lst= [["A","B","C","D","E"],["a","b","c","e"],["0","1","3","4"],["F","G","H","I","J"],["f","g","h","i","j"]]
# print(solution(lst))
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    lst= []
    for i in range(5):
        temp= list(input())
        lst.append(temp)
    # print(lst)
    print(f"#{test_case} {solution(lst)}")