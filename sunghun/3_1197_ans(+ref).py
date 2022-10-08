# 이코테 소스코드

import sys

# 부모 노드 찾기 (서로소 집합) ; 트리를 만들때 필요 => find
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 서로소 집합 간의 합집합 => union
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a 
    else:
        parent[a] = b
    
# 노드와 간선의 정보 저장
v, e = map(int, sys.stdin.readline().split())
parent = [0] * (v + 1)

edges = []
result = 0

for i in range(1, v + 1):
    parent[i] = i 

# 노드와 간선 가중치 값 저장
for _ in range(e):
    a, b, cost = map(int, sys.stdin.readline().split())
    edges.append((cost, a, b))
    
edges.sort()

# 노드 별로 꺼내서 부모 찾고 union 시켜줌
for edge in edges:
    cost, a , b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost 

# cost print
print(result)
    
