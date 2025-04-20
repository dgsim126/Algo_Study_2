from collections import deque

def solution(word):
    word= list(word)
    word= deque(word)
    result= ""

    while(word):
        temp= word.popleft()
        if(temp not in ("a", "e", "i", "o", "u")):
            result+=temp

    return result


## main ##
T = int(input())
for test_case in range(1, T + 1):
    word= input()
    print(f"#{test_case} {solution(word)}")
# word= "congratulation"
# print(solution(word))