# BFS로 풀기
import sys
from collections import deque
sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline 


def bfs(graph, x, visited):
    queue = deque([x])
    visited[x] = True 
    
    while queue:
        a = queue.popleft()
        for i in graph[a]: 
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

n = int(input()) # 컴퓨터 대수
m = int(input()) # 간선의 개수

graph = [[] for _ in range(n + 1)]

visited = [False] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(graph, 1, visited)

print(sum(visited) - 1)