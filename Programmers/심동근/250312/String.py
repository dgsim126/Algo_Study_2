'''
주어진 문자열의 첫 글자를 찾아 탐색 시작
만약 발견하면 그 뒤에것도 확인
- 발견이 뒤에서 시작되어 인덱스 밖으로 나갈 수 있기에 유의할 것
'''

def solution(short, long):
    first= short[0]
    cnt= 0

    for i in range(len(long)-len(short)+1):
        if(first==long[i]):
            if(short==long[i:i+len(short)]):
                # print(short, long[i:i+len(short)])
                cnt+=1

    return cnt

## main ##
for test_case in range(1, 11):
    num= input()
    short= input()
    long= input()
    result= solution(short, long)
    print(f"#{test_case} {result}")