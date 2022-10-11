import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())

graph = [[] for i in range(n+1)]
# 리스트형식으로 메모리 초과 해결 / 연결상태만 표시
for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
print(graph)
visited = [0]*(n+1)


def dfs(s):
    for i in graph[s]: # 해당 노드의 연결된 노드 들 확인 ex) graph[1] = [2,3] 1노드와 연결된 노드는 2,3
        if visited[i] == 0:  # 해당 노드와 연결된 노드중 하나에 방문을 하지 않았다면  노드 2와 3에 대해서 방문을 하지 않았다면
            visited[i] = s  # 해당 노드와 견결된 노드중 하나에 해당 노드를 방문 처리 노드 2와 3은 1노드와 연결되어있다.
            dfs(i)

dfs(1)

for x in range(2, n+1):
    print(visited[x])

# DFS 방식
# 문제에서 트리의 루트를 1이라고 정했기 때문에 1부터 DFS 탐색을 시작하고, 1과 연결되어 있는 Node들 중에 방문하지 않은 노드를 방문하는데, 
# 이 때 visited배열의 index에 탐색을 시작한 node(즉, 부모 노드) 를 저장한다. 이렇게 되면 visited에 0이 아닌 수가 저장이 되기 때문에 다시 방문하지 않는다.
# DFS를 사용한 풀이의 핵심은 DFS는 항상 부모에서 자식으로 이동한다는 점이다.

# 원래 알던 이차원배열에 모두 저장하는 방식 # 행렬방식 / 메모리 초과
# board = [[0]*(n+1) for i in range(n+1)]

# for i in range(n-1):
#     a, b = map(int, sys.stdin.readline().split())
#     board[a][b] = 1
#     board[b][a] = 1

# 시간초과 원인
# visited = [0]*(n+1)
# arr = []

# def dfs(s, prev):
#     arr.append((s, prev))
#     visited[s] = 1
#     for i in range(1, n+1):
#         if visited[i] == 0 and i in graph[s]:
#             dfs(i, s)