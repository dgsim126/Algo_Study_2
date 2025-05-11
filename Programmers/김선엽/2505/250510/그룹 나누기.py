# union find?

def solution(N, M, partners):
    number = N - len(set(partners))
    graph = []
    index = 0
    for i in range(M):
        if not graph:
            graph_ = [partners[index], partners[index+1]]
            graph_ = set(graph_)
            graph.append(graph_)
        else:
            team_ = False
            for team in graph:
                if partners[index] in team or partners[index+1] in team:
                    team_ = True
                    team.add(partners[index])
                    team.add(partners[index+1])
                    break
            if not team_:
                graph_ = [partners[index], partners[index + 1]]
                graph_ = set(graph_)
                graph.append(graph_)

        index += 2

    # print(graph)
    return len(graph) + number

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    partners = list(map(int, input().split()))
    answer = solution(N, M, partners)
    print(f"#{test_case} {answer}")