from itertools import combinations

n = int(input())
member = [n for n in range(n)] # 4명 -> 0~3
stat = [list(map(int, input().split())) for i in range(n)]
team_member_num = n//2

team_stat_gap = []
for case in combinations(member, team_member_num):
    team1 = list(case)
    team2 = []
    team1_stat = 0
    team2_stat = 0
    for check in range(n):
        if check not in team1:
            team2.append(check)
    for t1p1, t1p2 in combinations(team1, 2): # 팀1 모든 시너지
        team1_stat += (stat[t1p1][t1p2] + stat[t1p2][t1p1])

    for t2p1, t2p2 in combinations(team2, 2): # 팀2 모든 시너지
        team2_stat += (stat[t2p1][t2p2] + stat[t2p2][t2p1])

    team_stat_gap.append(abs(team1_stat - team2_stat))

print(min(team_stat_gap))