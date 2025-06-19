n = int(input())
answer = []
for i in range(1, n+1):
    new = ''
    lst = list(str(i).strip())
    if '3' in lst or '6' in lst or '9' in lst:
        for ls in lst:
            if ls in '369':
                new += '-'
            # else:
            #     new += ls

    if new == '':
        answer.append(str(i))
    else:
        answer.append(new)

print(*answer)