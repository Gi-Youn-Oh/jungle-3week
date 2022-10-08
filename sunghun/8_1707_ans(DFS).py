# https://ji-gwang.tistory.com/293
# 풀이방법 :
# 인접한 노드들을 기존 정점과 다른 그룹으로 설정해서 서로 연결되어 있는 노드 들 간에 같은 그룹이 되는 모순이 생기는지 확인

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline 

def dfs(start, group):
    global cycle
    
    # 만약 사이클이 true 라면 재귀 탈출
    if cycle:
        return
    
    visited[start] = group # 해당 그룹에 등록
    
    for i in graph[start]:
        if not visited[i]: # 방문하지 않았다면
            dfs(i, -group) # 다른 그룹으로 설정
        elif visited[start] == visited[i]:
            cycle = True 
            return


k = int(input()) # k는 test case

for _ in range(k):
    v, e = map(int, input().split()) # v는 정점의 개수, e는 간선의 개수
    graph = [[] for _ in range(v + 1)] # 빈 그래프 생성
    visited = [False] * (v + 1) # 방문한 정점 체크
    cycle = False
    
    for i in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    for i in range(1, v + 1):
        if not visited[i]: # 아직 방문하지 않았다면 
            dfs(i, 1) # dfs를 돈다.
            if cycle:
                break

    if cycle:
        print("NO")
    else:
        print("YES")