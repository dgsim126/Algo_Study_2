
def solution(word, lst):
    cnt= 0
    for i in range(len(lst)-len(word)+1):
        if(lst[i:i+len(word)]==word):
            cnt+=1

    return cnt

## main ##
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    input()
    word= input()
    lst= input()
    print(f"#{test_case} {solution(word, lst)}")
# word= "ti"
# lst= "Starteatingwellwiththeseeighttipsforhealthyeating,whichcoverthebasicsofahealthydietandgoodnutrition"
# print(solution(word, lst))