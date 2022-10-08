import sys
from collections import deque

# n : 정점 개수 / m : 간선 개수 / v : 탐색 시작할 번호
n, m, v = map(int, sys.stdin.readline().split())

# dfs 함수 출력
def dfs(graph, start, visited):
    # 현재 노드를 방문 처리
    visited[start] = True
    print(start, end=' ')
    
    # 다음 노드에 방문한 적이 없다면 방문 처리
    for i in range(n+1):
        if visited[i] == False and graph[start][i] == 1:
            dfs(graph, i, visited)
            

# bfs 함수 출력
def bfs(graph, start, visited):
    # 큐 구현을 위해 라이브러리 사용
    queue = deque([start])
    # 현재 노드 방문 처리
    visited[start] = True
    
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나 뽑아 출력
        q = queue.popleft()
        print(q, end=" ")
        # 해당 원소와 연결된 아직 방문하지 않은 원소들을 큐에 삽입
        for i in range(n+1):
            if visited[i] == False and graph[q][i] == 1:
                queue.append(i)
                visited[i] = True


graph = [[0] * (n + 1) for _ in range(n + 1)]
    
    
for i in range(m):
    a, b = map(int , input().split())
    graph[a][b] = graph[b][a] = 1 # 이 부분을 제대로 생각하지 못했음
    
# 방문 여부 리스트 만들기
visited = [False] * (n + 1)


dfs(graph, v, visited)
print()

# 방문 여부 리스트 만들기
visited = [False] * (n + 1)
bfs(graph, v, visited)
        