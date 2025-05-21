'''
1번을 기준으로
나와 연결된 녀석들을 모두 방문하고(방문한 적이 없다면) 방문 후 방문처리
'''


def solution(n, xxx):
    computers= [[-1]]

    for i in range(len(xxx)):
        temp1= xxx[i]
        temp2= [0]
        new_temp= temp2+temp1
        computers.append(new_temp)

    # print(computers) # [[-1], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1]] 0번 인덱스는 무시 1번부터 순회할 것, 맨 앞 값은 방문 여부

    def dfs(current):
        computers[current][0]= 1  # 방문 처리

        for i in range(1, n+1):
            if(computers[i][0]==0 and computers[current][i]==1):
                dfs(i)

    networks = 0

    # 1번부터 n번까지 순회(이렇게 dfs를 호출해야 모든 노드에서부터 시작해서 확인이 가능!)
    for i in range(1, n+1):
        if(computers[i][0]==0):
            dfs(i)
            networks+=1

    return networks

    # def dfs(computers, depth):
    #     global networks
    #
    #     for i in range(1, len(computers)):
    #         print(computers)
    #         if(computers[i][0]==0 and computers[i][depth]==1): # 새로운 네트워크
    #             if(depth==1):
    #                 networks+=1
    #
    #             computers[i][0]= 1 # 방문처리
    #
    #             dfs(computers, depth+1)
    #
    # dfs(computers, 1)
    #
    # return networks



## main ##
n= 3
computers= [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))