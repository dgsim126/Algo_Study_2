
def solution(word):
    N= len(word)


    # 회문 확인
    for i in range(N//2):
        if(word[i]!=word[N-1-i]):
            return "NO"

    # (N-1)/2 회문 확인
    slice_word= word[0:int((N-1)/2)]
    for i in range(len(slice_word)//2):
        if(slice_word[i]!=slice_word[len(slice_word)-1-i]):
            return "NO"

    return "YES"


## main ##
# word= "hello"
# word= "ababa"
# print(solution(word))
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    word= input()
    print(f"#{test_case} {solution(word)}")