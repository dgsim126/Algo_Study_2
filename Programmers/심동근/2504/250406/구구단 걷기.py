'''
두 수의 약수를 찾아야 한다.
약수 중 가장 중간의 값을 찾아야 한다. 1,2,3,4,6,12 12의 약수인 경우 3,4
'''
def solution(num):
    biggest= 0
    for i in range(1, int(num**(1/2))+1):
        if(num%i==0 and i>biggest):
            biggest= i

    return (biggest-1)+(num//biggest-1)

## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num= int(input())
    print(f"#{test_case} {solution(num)}")
# num= 1000000000000
# print(solution(num))