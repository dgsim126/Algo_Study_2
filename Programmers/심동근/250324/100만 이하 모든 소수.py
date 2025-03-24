'''
소수는 나 말고 나눠떨어지는 수가 없는 수?  전에 문제 풀 때 루트까지 나눠지지 않으면 소수로 판정했던 것이 기억이 남
그런데 모두 확인 시 100만 번까지 진행하게 될 경우 6억번 연산. 가능한가?
최대한 확인하는 경우를 줄여야 함
- 짝수 제외
'''


result= [2, 3, 5, 7, 11, 13, 17, 19]

for num in range(23, 1000001, 2):
    flag= True
    for i in range(2, int(num**(1/2))+1):
        if(num%i==0):
            flag= False
            break
    if(flag==True):
        result.append(num)

print(*result)





