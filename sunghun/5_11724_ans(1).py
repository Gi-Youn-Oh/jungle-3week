# https://ji-gwang.tistory.com/292
# DFS로 풀기

import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

# dfs로 그래프를 탐색
def dfs(start):
    # 해당 노드를 방문 체크
    visited[start] = True 
    
    # 해당 시작점을 기준으로 계속해서 그래프를 탐색
    for i in graph[start]:
        if not visited[i]:
            dfs(i)
            
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int ,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
# 방문 처리
visited = [False] * (1 + N)
count = 0 

# 1 ~ N번 노드를 각각 돌면서
for i in range(1, N + 1):
    if not visited[i]:
        if not graph[i]:
            count += 1 
            visited[i] = True
        else:
            dfs(i)
            count += 1
            
print(count)