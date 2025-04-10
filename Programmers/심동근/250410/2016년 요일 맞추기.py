def solution(month, date):
    months= [0,31,29,31,30,31,30,31,31,30,31,30,31]
    dates= sum(months[0:month])+date

    return (dates+3)%7

## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    month, date= map(int, input().split())
    print(f"#{test_case} {solution(month, date)}")
# month= 12
# date= 31
# print(solution(month, date))