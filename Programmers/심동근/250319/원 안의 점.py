'''
원점과의 거리를 이용해서 풀어야 할 것 같은데
어떤 방법을 선택해야 최소한의 점들로... 3초니까 그냥 해도 될 듯
하나의 사분면만 확인해도 된다.
'''
def check(x, y):
    return (x**2 + y**2)**(1/2)

def solution(radius):
    count= 0

    for x in range(1, radius+1):
        for y in range(1, radius+1):
            if(check(x,y)<=radius):
                count+=1
            else:
                break

    count*=4
    count+= (radius*4+1)

    return count

## main ##
T = int(input())
for test_case in range(1, T + 1):
    radius= int(input())
    print(f"#{test_case} {solution(radius)}")

# radius= 100
# print(solution(radius))