'''
A~B 사이의 수 중 제곱 펠린드롬 수 구하기
즉 수 N이 주어졌을 때 N, sqrt(N) 모두 펠린드롬이어야 함

펠린드롬 확인 연산 속도 vs sqrt 값이 정수인지 확인하는 연산
= 범위가 좁으므로 펠린드롬 확인이 더 빠름
'''

def check(val):
    len_= len(str(val))
    if(len_==1):
        return 1
    elif(len_==2 and val//10 == val%10):
        return 1
    elif(len_==3 and val//100 == val%10):
        return 1
    else:
        return 0


def solution(A, B):
    result= 0

    for i in range(A, B+1):
        if(i<10):
            if(i==1 or i==4 or i==9):
                result+=1
        elif(i<100):
            if(i//10 == i%10):
                if(i**(1/2)==int(i**(1/2))):
                    result+=check(int(i**(1/2)))

        elif(i<1000):
            if(i//100 == i%10):
                if(i**(1/2)==int(i**(1/2))):
                    result+=check(int(i**(1/2)))

    return result


## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    A, B= map(int, input().split())
    print(f"#{test_case} {solution(A, B)}")
# A= 10
# B= 99
# print(solution(A, B))