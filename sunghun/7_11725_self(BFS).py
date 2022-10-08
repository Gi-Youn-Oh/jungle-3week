import sys
from collections import deque

input = sys.stdin.readline 

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True 
    
    while queue:
        x = queue.popleft()
        
        for i in graph[x]:
            if visited[i] != True:
                queue.append(i)
                parent[i] = x
                visited[i] = True


n = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 리스트 설정
visited = [False] * (n + 1)

# 부모 원소 설정
parent = [0] * (n + 1)
for i in range(n+1):
    parent[i] = i

bfs(graph, 1, visited)
# print(parent) # 확인

for i in range(2, n + 1):
    print(parent[i])