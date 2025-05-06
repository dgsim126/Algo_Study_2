def solution(alpa):
    perfect= "abcdefghijklmnopqrstuvwxyz"
    count= 0

    for i in range(len(alpa)):
        if(alpa[i]!=perfect[i]):
            return count
        else:
            count+=1

    return count


## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    alpa= input()
    print(f"#{test_case} {solution(alpa)}")


# alpa= "zabcdefghijklmnopqrstu"
# print(solution(alpa))