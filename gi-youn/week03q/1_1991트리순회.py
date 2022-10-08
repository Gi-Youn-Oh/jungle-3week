import sys
input = sys.stdin.readline
N = int(input().strip())
tree = {}  # dictionay  {A:[B,C]}
 
for n in range(N): 
    root, left, right = input().strip().split() # 루트 노드 왼쪽노드 우측 노드
    tree[root] = [left, right]    
 
 
def preorder(root): # 전위순회
    if root != '.':     
        print(root, end='')  # root
        preorder(tree[root][0])  # left
        preorder(tree[root][1])  # right
 
 
def inorder(root): # 중위순회
    if root != '.':
        inorder(tree[root][0])  # left
        print(root, end='')  # root
        inorder(tree[root][1])  # right
 
 
def postorder(root): # 후위순회
    if root != '.':
        postorder(tree[root][0])  # left
        postorder(tree[root][1])  # right
        print(root, end='')  # root
 
 
preorder('A')
print()
inorder('A')
print()
postorder('A')



