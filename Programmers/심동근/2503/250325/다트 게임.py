

def check_radius(x, y):
    return (x**2 + y**2)**0.5

def get_point(radius):
    lst= [20,40,60,80,100,120,140,160,180,200]
    point= -1

    if (lst[0] >= radius):
        point = lst[0]
        return -(point/20)+11

    for i in range(len(lst)-1):
        if(lst[i]< radius and radius <= lst[i+1]):
            point= lst[i+1]
            break

    if(point==-1):
        return 0

    return -(point/20)+11

def solution(N, x_index, y_index):
    result= 0

    for i in range(len(x_index)):
        # radius= check_radius(x_index[i], y_index[i])
        radius= (x_index[i]**2 + y_index[i]**2)**0.5
        result+= get_point(radius)

    return int(result)


## main ##
T = int(input())
for test_case in range(1, T + 1):
    N= int(input())
    x_index= []
    y_index= []
    for i in range(N):
        x, y= map(int, input().split())
        x_index.append(x)
        y_index.append(y)
    print(f"#{test_case} {solution(N, x_index, y_index)}")

# N= 5 # 화살의 개수
# x_index= [80, 117, 98, -86, -121]
# y_index= [-14, 12, -69, 21, 99]
# print(solution(N, x_index, y_index))