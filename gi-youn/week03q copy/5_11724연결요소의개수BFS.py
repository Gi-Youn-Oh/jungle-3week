import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

N, M = map(int, input().split())
graph = [[]for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문처리
visited = [False] * (1 + N)
count = 0 # 컴포넌트 그래프 개수 저장

# 1~N 번 노드를 각각 돌면서
for i in range(1, N + 1):
    if not visited[i]: #만약 방문하지 않았다면
        if not graph[i]: # 만약 그래프가 비어있다면
            count += 1
            visited[i] = True # 방문처리
        else: # 만약 그래프가 비어있지 않다면 (어느 점과 연결된 점이 있다면)
            bfs(i)
            count +=1

print(count)