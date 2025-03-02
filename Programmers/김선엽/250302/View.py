from collections import deque

def solution(N, buildings):
    queue = deque([])
    answer = 0
    for i in range(N):
        if len(queue) < 2:
            queue.append([buildings[i], 0])
        else:
            height1, able1 = queue.popleft()
            height2, able2 = queue.popleft()

            able = 0

            if height1 >= height2:
                if buildings[i] >= height1:
                    able1 = 0
                    able = buildings[i] - height1
                elif buildings[i] < height1 and buildings[i] > height2:
                    able = 0
                    able_can = height1 - buildings[i]
                    if able_can < able1:
                        able1 = able_can
                elif buildings[i] <= height2:
                    able = 0
                
            else:
                if buildings[i] >= height2:
                    able2 = 0
                    able = buildings[i] - height2
                elif buildings[i] < height2 and buildings[i] >= height1:
                    able = 0
                    able_can = height2 - buildings[i]
                    if able_can < able2:
                        able2 = able_can
                elif buildings[i] < height1:
                    able = 0
            
            answer += able1
            queue.append([height2, able2])
            queue.append([buildings[i], able])

    return answer

N = int(input())
buildings = list(map(int, input().split()))



# print(solution(10, [0,0, 254, 185, 76, 227, 84, 175, 0, 0])) # 111
# print(solution(10, [0, 0, 251, 199, 176, 27, 184, 75, 0, 0])) # 60
# print(solution(11, [0, 0, 118, 90, 243, 178, 99, 100, 200, 0, 0])) #165