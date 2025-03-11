'''
각 줄의 문자열을 8개로 나눈다.
8개로 나눈 문자열을 각각 십진수로 변환한다.
계산한다
'''

def solution(n,m,code):
    for i in range(len(code)-1, -1, -1):
        for j in range(len(code[0])-1, -1, -1):
            if(code[i][j]=="1"):
                real_code= code[i][j-55:j+1]
                break
    # print(real_code)

    lst= []
    for i in range(8):
        lst.append(real_code[i*7:i*7+7])
    # print(lst) # ['0111011', '0110001', '0111011', '0110001', '0110001', '0001101', '0010011', '0111011']

    num= []
    for i in range(len(lst)):
        if lst[i] == "0001101":
            num.append(0)
        elif lst[i] == "0011001":
            num.append(1)
        elif lst[i] == "0010011":
            num.append(2)
        elif lst[i] == "0111101":
            num.append(3)
        elif lst[i] == "0100011":
            num.append(4)
        elif lst[i] == "0110001":
            num.append(5)
        elif lst[i] == "0101111":
            num.append(6)
        elif lst[i] == "0111011":
            num.append(7)
        elif lst[i] == "0110111":
            num.append(8)
        elif lst[i] == "0001011":
            num.append(9)
    # print(num)

    sum_= sum(num)
    result= (num[0]+num[2]+num[4]+num[6])*3 + (num[1]+num[3]+num[5]+num[7])
    # print(result)

    if(result%10==0):
        return sum_
    else:
        return 0



## main ##
T = int(input())
for test_case in range(1, T + 1):
    n, m= input().split()
    code= []
    for i in range(int(n)):
        temp= input()
        code.append(temp)

    result= solution(int(n), int(m), code)

    print(f"#{test_case}, {result}")


# n= 16
# m= 80
# code= [
# "00000000000000000000000000000000000000000000000000000000000000000000000000000000",
# "00000000000000000000000000000000000000000000000000000000000000000000000000000000",
# "00000000000000000000000000000000000000000000000000000000000000000000000000000000",
# "00000000000000000000000000000000000000000000000000000000000000000000000000000000",
# "00000000000000000000000000000000000000000000000000000000000000000000000000000000",
# "00000000000000000000000000000000000000000000000000000000000000000000000000000000",
# "00000000000000011101101100010111011011000101100010001101001001101110110000000000",
# "00000000000000011101101100010111011011000101100010001101001001101110110000000000",
# "00000000000000011101101100010111011011000101100010001101001001101110110000000000",
# "00000000000000011101101100010111011011000101100010001101001001101110110000000000",
# "00000000000000011101101100010111011011000101100010001101001001101110110000000000",
# "00000000000000011101101100010111011011000101100010001101001001101110110000000000",
# "00000000000000011101101100010111011011000101100010001101001001101110110000000000",
# "00000000000000000000000000000000000000000000000000000000000000000000000000000000",
# "00000000000000000000000000000000000000000000000000000000000000000000000000000000",
# "00000000000000000000000000000000000000000000000000000000000000000000000000000000"
# ]
# print(solution(n,m,code))