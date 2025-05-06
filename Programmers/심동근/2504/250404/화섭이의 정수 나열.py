'''
N=1000 길이가 1000까지 가능
주어진 문자열을 1개씩 끊어서 읽어온다. 빠진 숫자가 있다면 그 중 가장 작은 값이 정답
2개씩 끊을 경우에도

이거보다 빠른 방법이 없을 거 같은데...

끊어낸 값을 lst에 넣고, 0부터 시작해 비교
'''
from collections import deque

def solution(N, word):
    if(len(word)==1):
        if(word=="0"):
            return 1
        else:
            return 0

    lst= []
    current_value= 0
    for i in range(1, len(word)):
        for j in range(0, len(word)-i+1):
            lst.append(word[j:j+i])
        # print(lst)
        lst= list(set(lst))
        lst.sort()
        # print(lst)
        # print()
        for j in range(len(lst)):
            if(lst[j]==str(current_value)):
                # print(lst[j], str(current_value))
                current_value+=1
            elif(int(lst[j])<current_value):
                continue
            else:
                # print(lst[j], str(current_value))
                return current_value
        lst= []
    return current_value

## main ##
## main ##
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    word = []
    while len(word) < N:
        word.extend(input().split())

    word = ''.join(word)
    print(f"#{test_case} {solution(N, word)}")

# N= 2
# word= "013"
# # word= "7275474458157705620434110616621792469362805976314919126429783955233840682550671851481373353060653222"
# print(solution(N, word))