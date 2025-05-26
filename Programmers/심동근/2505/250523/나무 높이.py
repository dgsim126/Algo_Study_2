'''
최소 날짜 수,
need를 돌면서
홀수날은 1씩 감소하고, 짝수날은 2씩 감소하면 된다.

어떻게 해야할까?
그냥 뒤에서부터 1씩 뺴고, 2씩 빼고
만약에 맨 앞의가 2를 뺴야하는데 1밖에 없다면 뒤에거 먼저
'''


def solution(N, trees):
    goal= max(trees)
    need= []
    day= 1

    for i in range(N):
        need.append(goal-trees[i])

    temp= need[:]
    temp.append(0)
    temp= set(temp)
    if(len(temp)==1):
        return 0

    while (len(need) != 0 and need[-1] == 0):
        need.pop()

    print(need) # [8, 7, 0, 5]
    print()
    print()

    while(need):
        print(day, "일 경과")
        print(need)


        if(day%2==1): # 홀수날
            temp= set(need)
            if((len(temp)==1 and 2 in temp) or (len(temp)==2 and 0 in temp and 2 in temp)): # 만약 현재 기준으로 set으로 변경했을 때, 0,2만 있거나 2만 있다면 바로 day+=2 후 return
                day+=1
                return day
            else:
                need[-1]-=1

        else: # 짝수날
            for i in range(len(need)-1, -1, -1):
                if(need[i]>1):
                    need[i]-=2
                    flag= False
                    break



        while (len(need)!=0 and need[-1]==0):
            need.pop()

        if(len(need)==0):
            return day

        day += 1
        print(need)
        print()

    return day


## main ##
N= 20
trees= [4, 5, 3, 4, 2, 4, 4, 3, 5, 2, 2, 3, 5, 5, 5, 2, 5, 2, 5, 5]
print(solution(N, trees))
# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     N= int(input())
#     trees= list(map(int, input().split()))
#     print(solution(N, trees))