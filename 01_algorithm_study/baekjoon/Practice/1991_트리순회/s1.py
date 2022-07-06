import sys
sys.stdin = open('input.txt')

N = int(input()) # 이진트리 노드의 개수
tree = {}

# 함수 만들기
def preorder(root):
    if root != '.':
        print(root, end='')  # root
        preorder(tree[root][0])  # left
        preorder(tree[root][1])  # right


def inorder(root):
    if root != '.':
        inorder(tree[root][0])  # left
        print(root, end='')  # root
        inorder(tree[root][1])  # right


def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

# 읽어오기
for i in range(N):
    root, left, right = map(str, input().split())
    tree[root] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')
