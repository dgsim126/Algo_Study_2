'''
맨 앞의 값을 pop한 후 word[0]과 같은지 확인
- 같으면 pop 한 번 더
- 다르면 위의 동작 반복
'''

from collections import deque

def solution(word):
    dic= {}

    for i in range(len(word)):
        if(word[i] not in dic):
            dic[word[i]]= 1
        else:
            dic[word[i]]+=1

    result= []

    for key, value in dic.items():
        if(value%2!=0):
            result.append(key)

    if(len(result)==0):
        return "Good"

    return "".join(sorted(result))

## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    word= input()
    print(f"#{test_case} {solution(word)}")

# word= "qnwerrewmqq"
# print(solution(word))