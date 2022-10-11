# root를 저장하는 Vroot 배열을 생성한다. (여기서 root는 연결요소중 가장 작은 값, 처음에는 자기 자신을 저장)
# 간선들(Elist)을 가중치 기준으로 정렬한다.
# 간선들이 이은 두 정점을 find함수를 통해 두 root(sRoot, eRoot)를 찾는다.
# 두 root가 다르다면 큰 root값을 작은 root값으로 만들어 연결되게 해준다.
# 가중치를 더한다.

import sys
input = sys.stdin.readline
 
v, e = map(int, input().split())
parent = [i for i in range(v+1)] # 루트 노드 모음
#
# parent = [0]*(v+1)
# for i in range(1, v+1):
#     parent[i] = i
edges = [] #간선 정보 모음
for _ in range(e):  # 간선수에대해서  정보 입력받기
    edges.append(list(map(int, input().split())))
#
#for _ in range(e):
#   a,b, cost = map(int,input().split())
   # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
#   edges.append((cost,a,b))
 
edges.sort(key=lambda x: x[2])
 #
 #edges.sort()
 
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]
 #
 # def find_parent(parent,x):
    # if parent[x] != x:
    #     parent[x] = find_parent(parent, parent[x])
    # return parent[x]

 
answer = 0
for s, e, w in edges:
    sRoot = find(s)
    eRoot = find(e)
    if sRoot != eRoot:
        if sRoot > eRoot:
            parent[sRoot] = eRoot
        else:
            parent[eRoot] = sRoot
        answer += w
 
#  result = 0
# for edge in edges:
#     cost, a, b = edge
#     if find_parent(parent, a) != find_parent(parent, b):
#         union_parent(parent, a, b)
#         result += cost
print(answer)