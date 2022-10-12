# 정점의 개수 간선의수 탐색 시작 노드번호
N, M, V = map(int, input().split())

# 행렬 만들기
graph = [[0]*(N + 1) for _ in range(N+1)]
for i in range(M):
    a,b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

# 방문 리스트 행렬
visited1 = [0]*(N+1)
visited2 = visited1.copy()

#dfs 함수 만들기
def dfs(V):
    visited1[V] = 1 # 방문처리
    print(V, end=' ')
    for i in range(1, N+1): #연결된 작은 수부터 확인해서 재귀
        if graph[V][i] == 1 and visited1[i] == 0:  # 노드와 연결된 노드중에서 방문하지 않은 노드가 있다면
            dfs(i)

def bfs(V):
    queue = [V]
    visited2[V] = 1 #방문처리
    while queue:
        V = queue.pop(0) # 방문 노드 제거
        print(V, end = ' ')
        for i in range(1, N+1):
            if (visited2[i] == 0 and graph[V][i] ==1):
                queue.append(i)
                visited2[i] = 1

dfs(V)
print()
bfs(V)