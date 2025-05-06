'''
버스 노선이 주어졌을 때, 각 정류장에 몇 개의 버스가 다니는지 구하면 된다.
의문: j를 왜 굳이 뒤에 입력받지?
- 순서가 이상하게 들어오거나 누락이 있을 수 있다고 가정하고 문제 해결할 것

== 틀린 이유: [1,5,3,3,3] bus_stop의 값이 중복으로 들어올 수 있음(쓰레기 문제)
'''
def solution_false(N, starts, ends, P, bus_stop):
    bus_stop_count= [0]*P

    for i in range(N):
        start= starts[i]
        end= ends[i]
        for value in range(start, end+1):
            if(value in bus_stop):
                index_= bus_stop.index(value)
                bus_stop_count[index_]+=1

    return bus_stop_count

def solution(N, starts, ends, P, bus_stop):
    bus_stop_count = [0] * P

    for i in range(P):  # 정류장 하나씩 확인
        stop = bus_stop[i]
        for j in range(N):  # 모든 버스 노선 확인
            if starts[j] <= stop <= ends[j]:
                bus_stop_count[i] += 1

    return bus_stop_count

## main ##
T = int(input())
for test_case in range(1, T + 1):
    N= int(input())
    start= []
    end= []
    bus_stop= []
    for i in range(N):
        a, b= map(int, input().split())
        start.append(a)
        end.append(b)

    P= int(input())
    for i in range(P):
        bus_stop.append(int(input()))

    result= solution(N, start, end, P, bus_stop)
    print(f"#{test_case}", *result)

# N= 2 # 버스 노선
# start= [1, 2]
# end= [3, 5]
# P= 5 # 버스 정류장의 개수
# bus_stop= [1,5,3,3,3]
# print(solution(N, start, end, P, bus_stop))