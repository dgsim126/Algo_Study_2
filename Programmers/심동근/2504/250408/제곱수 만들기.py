'''
2억번 연산 가능
10,000,000
A에다가 어떤 값을 곱했을 때, 그 결과가 거듭제곱이 되어야 한다
'''


def solution(A):
    double= []

    i= 1
    while(True):
        val= i*i
        if(val>10000000):
            break
        double.append(val)
        i+=1
    # print(double)
    len_= len(double)

    i= 1
    current_index= 0
    while(current_index<len_):
        val= A*i
        if(val>double[current_index]):
            current_index+=1
        elif(val<double[current_index]):
            i+=1
        else:
            return i

## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    A= int(input())
    print(f"#{test_case} {solution(A)}")
# A= 1
# print(solution(A))