'''
규칙을 찾는 문제같다.
7X7 사이즈를 예로 들면, 첫 줄에서부터 순서대로
 - [3:4], [2:5], [1:6], [0,7], [1:6], [2:5], [3:4] 라는 것을 알 수 있다.
 위의 규칙대로 만들자!

'''
def solution(N, farm):
    farms= []
    for value in farm:
        temp= (list(value))
        farms.append(list(map(int, temp)))
    # print(farms)

    default= N//2
    start_point= default
    end_point= default+1
    result= 0

    for i in range(N//2+1): # 증가
        # print("up", farms[i][start_point:end_point])
        result+=sum(farms[i][start_point:end_point])
        start_point-=1
        end_point+=1

    temp= N//2+1
    start_point+=2
    end_point-=2
    for i in range(N//2): # 감소
        # print("down", farms[i+temp][start_point:end_point])
        result+=sum(farms[i+temp][start_point:end_point])
        start_point+=1
        end_point-=1

    return result


## main ##
# N= 5
# farm= ["14054", "44250", "02032", "51204", "52212"]
# print(solution(N, farm))

T = int(input())
for test_case in range(1, T + 1):

    N= int(input())
    farm= []
    for i in range(N):
        temp= input()
        farm.append(temp)

    result= solution(N, farm)
    print(f"#{test_case} {result}")
