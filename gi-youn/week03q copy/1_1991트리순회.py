# 핵심
# 1. 전위순회, 중위순회, 후위순회에 대한 개념 인지
# 2. 노드 간의 관계를 딕셔너리 형태로 표시 (활용)
# 3. 재귀함수 활용
# 4. 출력 방식

import sys
input = sys.stdin.readline
N = int(input().strip())
tree = {} # 딕셔너리 형태로 노드 연결 상태 표시

for n in range(N):
    root, left, right = input().strip().split() #루트 왼쪽 오른쪽
    tree[root] = [left,right] 
# print(tree)
# {'A': ['B', 'C'], 'B': ['D', '.'], 'C': ['E', 'F'], 'E': ['.', '.'], 'F': ['.', 'G'], 'D': ['.', '.'], 'G': ['.', '.']}
def preorder(root): # 전위순회
    if root != '.':
        print(root,end='') # root 공백없이 출력
        preorder(tree[root][0]) #left
        preorder(tree[root][1]) #right

def inorder(root): # 중위순회
    if root != '.':
        inorder(tree[root][0]) #left
        print(root, end='') #root
        inorder(tree[root][1]) #right

def postorder(root): #후위순회
    if root != '.':
        postorder(tree[root][0]) # left
        postorder(tree[root][1]) # right
        print(root, end = '') # root

preorder('A')
print()
inorder('A')
print()
postorder('A')