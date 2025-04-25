'''
루트 노드= 짝수일 때(N//2 +1), 홀수일 때(n//2 +1)

이진 탐색 트리를 직접 구현해야 하나?

'''

def solution(N):
    tree = [0] * (N + 1)
    value = [i for i in range(1, N + 1)]
    idx = [0]  # 값을 채울 인덱스 (리스트로 감싼 이유는 중위 순회에서 값 유지)

    def inorder(node):
        if node > N:
            return
        inorder(node * 2)           # 왼쪽 자식 inorder(1), inorder(2), inorder(4)
        tree[node] = value[idx[0]]  # 현재 노드에 값 채우기
        idx[0] += 1
        inorder(node * 2 + 1)       # 오른쪽 자식

    inorder(1)
    print("tree", tree)
    print("value", value)
    print(idx)
    return tree[1], tree[N // 2]


## main ##
N= 6
print(solution(N))