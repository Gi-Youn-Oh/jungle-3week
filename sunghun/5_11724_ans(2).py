# https://ji-gwang.tistory.com/292
# BFS로 풀기

from collections import deque
import sys 

input = sys.stdin.readline 


def bfs(graph, start, visited):
    
    queue = deque([start])
    visited[start] = True 
    
    while queue:
        v = queue.popleft()
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True 
                
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
# 방문 처리
visited = [False] * (1 + n)
count = 0

# 1 ~ n번 노드를 각각 돌면서
for i in range(1, n + 1):
    if not visited[i]:
        if not graph[i]:
            count += 1 
        else:
            bfs(graph, i, visited)
            count += 1
            
print(count)