test_place = int(input()) # 시험장 수
testers = list(map(int, input().split())) # 응시자 수
first, second = map(int, input().split()) # 총 감독관이 감시할 수 있는 응시자 수, 부감독관이 감시할 수 있는 응시자 수

num = 0
for tester in testers:
    num += 1
    left = tester - first

    if left > 0:
        if left % second == 0:
            num += (left // second)
        else:
            num += ((left // second) +1)

print(num)