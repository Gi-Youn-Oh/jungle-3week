# 기본적인 트리 순회방법에 대해 정확하고 확실히 기억하자.
# 전위순회, 중위순회, 후위순회
# 루트,왼쪽,오른쪽 / 왼쪽,루트,오른쪽 / 왼쪽, 오른쪽, 루트
# 각 순회방법에 대한 함수정의
# 순회는 재귀함수로 구현
# 단순 리스트 형식에서 튜플, 딕셔러니 형태에 대한 사고를 넓혀 생각하자.

import sys
input = sys. stdin.readline
tree = {} # dictionary {A:[B,C]}

for n in range(N):
    root, left, right = input().strip().split()
    tree[root] = [left,right] # {A:[B,C]}

# 각 순회 방식이 어떻게 이루어지는 지에 대한 이해가 먼저 이루어져야 코드이해가 쉽다.
def preorder(root): # 전위순회
    if root !='.':
        print(root, end='') #root
        preorder(tree[root][0]) # left
        preorder(tree[root][1]) # right

def inorder(root): # 중위순회
    if root !='.':
        inorder(tree[root][0]) # left
        print(root,end='') # root
        inorder(tree[root][1]) #right

def postorder(root): # 후위순회
    if root !='.':
        postorder(tree[root][0]) #left
        postorder(tree[root][1]) #right
        print(root,end= '') # root
#G를 마지막으로 받아서 해당 순회에 대한 출력을 하기위해 A를 대입해주고
# 칸구분을 위해서 빈칸 출력을 해준다.

preorder('A')
print()
inorder('A')
print()
postorder('A')