import sys

sys.setrecursionlimit(20000)
input = sys.stdin.readline


def dfs(start, group):
    global error

    # 만약 사이클이 true라면 재귀탈출
    if error:
        return

    visited[start] = group  # 해당 그룹으로 등록

    for i in graph[start]:
        if not visited[i]:
            dfs(i, -group)  # 다른 그룹으로 설정
        elif visited[start] == visited[i]:  # 인접한데 같은 그룹이라면
            error = True  # 에러값 True
            return  # 그후 재귀 리턴


K = int(input())

for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]  # 빈 그래프 생성
    visited = [False] * (V + 1)  # 방문한 정점 체크
    error = False

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, V + 1): # 모든 정점에 대해 확인 
        if not visited[i]:  # 만약 아직 방문하지 않았다면
            dfs(i, 1)  # dfs를 돈다.
            if error:  # 만약 에러가 참이라면
                break  # 탈출

    if error:
        print('NO')
    else:
        print('YES')

# point1. 인접한 노드가 간선이 같은 색이면 안된다 > 두 그룹으로 나누어서 / 같은 그룹에 있으면 x 아니면 o
# point2. 비 연결 그래프일 경우 모든 정점에 대해 확인 필요