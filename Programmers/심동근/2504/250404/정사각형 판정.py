def solution(N, lst):

    blocks= []
    for i in range(N):
        for j in range(N):
            if(lst[i][j]=="#"):
                blocks.append((i,j))

    min_y = min(x for x, y in blocks)
    max_y = max(x for x, y in blocks)
    min_x = min(y for x, y in blocks)
    max_x = max(y for x, y in blocks)

    if((max_y- min_y+1)!=(max_x- min_x+1)):
        return 'no'


    for i in range(min_y, max_y + 1):
        for j in range(min_x, max_x + 1):
            if lst[i][j] != '#':
                return 'no'

    if(len(blocks)!=(max_y- min_y+1)*(max_x- min_x+1)):
        return 'no'

    return 'yes'


## main ##
T = int(input())
for test_case in range(1, T + 1):
    N= int(input())
    lst= []
    for i in range(N):
        lst.append(input())
    print(f"#{test_case} {solution(N, lst)}")