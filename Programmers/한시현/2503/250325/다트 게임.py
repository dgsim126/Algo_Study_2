T = int(input())
for test_case in range(1, T + 1):
    arrows = int(input()) # 화살 수
    locations = []
    for i in range(arrows):
        xy = list(map(int, input().split()))
        locations.append(xy)

    rs = [20,40,60,80,100,120,140,160,180,200]
    scores = []
    for r in rs:
        scores.append(11-r/20) # p = 11 - 반지름/20

    total_score = 0
    for l in locations:
        dis = (l[0]**2 + l[1]**2)**0.5
        if dis <= rs[0]:
            total_score += scores[0]
        elif rs[0] < dis <= rs[1]:
            total_score += scores[1]
        elif rs[1] < dis <= rs[2]:
            total_score += scores[2]
        elif rs[2] < dis <= rs[3]:
            total_score += scores[3]
        elif rs[3] < dis <= rs[4]:
            total_score += scores[4]
        elif rs[4] < dis <= rs[5]:
            total_score += scores[5]
        elif rs[5] < dis <= rs[6]:
            total_score += scores[6]
        elif rs[6] < dis <= rs[7]:
            total_score += scores[7]
        elif rs[7] < dis <= rs[8]:
            total_score += scores[8]
        elif rs[8] < dis <= rs[9]:
            total_score += scores[9]
        else:
            total_score += 0

    print(f'#{test_case} {int(total_score)}')