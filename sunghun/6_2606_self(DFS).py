# DFS로 풀기
import sys

sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = True 
    
    for x in graph[v]:
        if visited[x] == False:
            visited[x] = True 
            dfs(graph, x, visited) 

n = int(input()) # 컴퓨터의 수
m = int(input()) # 간선의 수 

graph = list([] for _ in range(n + 1))
visited = [False] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(graph, 1, visited)
# print(graph)
print(sum(visited) - 1)