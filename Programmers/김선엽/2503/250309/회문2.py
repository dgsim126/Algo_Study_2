for _ in range(1, 11):  # 10개 테스트
    test = int(input())
    board = [[] for i in range(100)]  # 열을 행 형태로 저장하기 위한 공간
    maxNum = 0

    for i in range(100):  # 행
        line = [i for i in input()]
        for l in range(100):  # 각 열 값을 append하여 행으로 만들기
            board[l].append(line[l])

        for j in range(100, 3, -1):  # 100부터 2까지 회문 길이를 줄여가며 탐색
            tf = False  # 회문을 찾았는지 체크
            for k in range(0, 101-j):
                temp = line[k:k+j]  # 회문이 될 가능성 있는 것

                if temp[:j//2] == temp[j//2:][::-1] or temp[:j//2] == temp[j//2+1:][::-1]:  # 회문
                    tf = True
                    break
            if tf:  # 회문 찾았을 때
                maxNum = max(maxNum, j)  # 지금까지 찾은 길이 vs 해당 행 가장 긴 것
                break  # 가장 먼저 찾은 회문이 그 행의 가장 큰 수이므로 다음 행 탐색

    for i in range(100):  # 열, 행에서 얻어낸 결과를 가지고 수행
        for j in range(100, 3, -1):  # 100부터 2까지 회문 길이를 줄여가며 탐색
            tf = False  # 회문을 찾았는지 체크
            for k in range(0, 101-j):
                temp = board[i][k:k+j]  # 회문이 될 가능성 있는 것

                if temp[:j//2] == temp[j//2:][::-1] or temp[:j//2] == temp[j//2+1:][::-1]:  # 회문
                    tf = True
                    break
            if tf:  # 회문 찾았을 때
                maxNum = max(maxNum, j)  # 지금까지 찾은 길이 vs 해당 열 가장 긴 것
                break  # 가장 먼저 찾은 회문이 그 열의 가장 큰 수이므로 다음 열 탐색

    print("#{} {}".format(test, maxNum))