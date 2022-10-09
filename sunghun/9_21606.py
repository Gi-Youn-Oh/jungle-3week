# 21606 아침산책
import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

def dfs(graph, v, visited):
    global count
    visited[v] = True
    
    if graph[v] == False: # 그래프가 비어있을 때는 바로 리턴
        return
    
    for node, ie in graph[v]:
        if ie == 0 and visited[node] == False:
            visited[node] = True 
            dfs(graph, node, visited)

        if ie == 1 and visited[node] == False:
            visited[node] = True
            count += 1 

    return 


# 정점의 수
n = int(input())

# Internal or External
e = str(input().strip())

ie = [0]
for i in range(1, len(e) + 1):
    ie.append(int(e[i-1]))


graph = [[] for _ in range(n + 1)]
for _ in range(1, n):
    a, b = map(int, input().split())
    graph[a].append((b, ie[b])) # 튜플형식으로 간선, 실내/실외 구분
    graph[b].append((a, ie[a])) # 튜플형식으로 간선, 실내/실외 구분

count = 0

# 차례대로 dfs 시작하기
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    if ie[i] != 0:
        dfs(graph, i, visited) 
    
print(count)