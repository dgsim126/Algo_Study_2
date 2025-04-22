Test_case=int(input())

def function(N):
    if N%10==0:
        if N==10: #N=10일때 1반환
            return 1
        elif N==20: #20x20은 3반환 
            return 3
        else:
            return function(N-10)+(2*function(N-20))
    else:
        print("10의 배수만 입력하세요")

for t in range(1, Test_case+1):
    N=int(input())
    count=function(N)
    print("#{} {}".format(t,count))
출처: https://totoma3.tistory.com/126 [토토모의 분석일지:티스토리]