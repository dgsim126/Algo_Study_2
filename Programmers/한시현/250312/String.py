T = 10
for _ in range(1, T + 1):
    test_case = int(input())
    check = input()
    sentence = input()

    count = 0
    for i in range(len(sentence)):
        if sentence[i] == check[0]:
            if i + len(check) <= len(sentence) and sentence[i:i+len(check)] == check:
                count += 1

    print(f"#{test_case} {count}")