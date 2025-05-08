'''
lst의 모든 값들을 B만큼 줄인다.
lst만큼 result에 추가
나머지 lst를 돌면서 //C를 하고 %값이 있다면 +1하여 result에 추가
'''

def solution(N, lst, B, C):
    result= N
    for i in range(N):
        lst[i]-=B

    for i in range(N):
        if(lst[i]<=0):
            continue
        temp= lst[i]//C
        if(lst[i]%C!=0):
            temp+=1
        result+=temp

    return result



## main ##
N= int(input())
lst= list(map(int, input().split()))
B, C= map(int, input().split())
# N= 5 # 시험장의 수
# lst= [2,2,4,2,2] # 각 시험장 응시자 수
# B= 1 # 총감독이 감시할 수 있는 응시자 수
# C= 2 # 부감독이 감시할 수 있는 응시자 수
print(solution(N, lst, B, C))