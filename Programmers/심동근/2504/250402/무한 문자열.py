
def solution(S, T):
    long= ""
    short= ""
    if(len(S)>len(T)):
        long= S
        short= T
    else:
        long= T
        short= S

    ## 빠른 결과 반환을 위한 ##
    if(short!=long[0:len(short)]):
        return "no"

    ## 빠른 결과 반환을 위한 ##
    if(set(long)!=set(short)):
        return "no"

    current_long= long
    current_short= short
    while(len(current_long)!=len(current_short)):
        if(len(current_long)>len(current_short)):
            current_short+=short
        else:
            current_long+=long

    if(current_long==current_short):
        # print(current_long)
        return "yes"
    else:
        return "no"

## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    S, T= input().split()
    print(f"#{test_case} {solution(S, T)}")


# S= "ababab"
# T= "abab"
# print(solution(S, T))
