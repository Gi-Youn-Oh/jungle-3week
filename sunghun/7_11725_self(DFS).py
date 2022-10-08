import sys

sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline 

# dfs 함수 출력
def dfs(graph, v, visited):
    visited[v] = True
    
    for i in graph[v]:
        if visited[i] != True:
            parent[i] = v
            visited[i] = True
            dfs(graph, i, visited)
            

n = int(input())
graph = [[] for _ in range(n + 1)] 

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)

# 부모 리스트 생성
parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i # 일단 자기 자신으로 생성
    
dfs(graph, 1, visited)
# print(parent) # 확인용

for i in range(2, n+1):
    print(parent[i])