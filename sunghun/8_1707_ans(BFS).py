# https://ji-gwang.tistory.com/293
# DFS와 풀이과정은 유사함
# 인접한 노드들을 다른 그룹으로 설정하여 만약 인접 그룹 간에 동일 그룹이 보이면 바로 False return

import sys
from collections import deque

input = sys.stdin.readline

def bfs(start, group):
    queue = deque([start])
    visited[start] = group
    
    while queue:
        
        x = queue.popleft()
        
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = -1 * visited[x]
            elif visited[i] == visited[x]: # 이 라인을 포함하여 두 줄이 생각하기 어려울 것 같음
                return False # False 값을 바로 리턴함
            
    return True # return True를 생각하는 것 자체가 쉽지 않을 것 같다



k = int(input()) # 테스트 케이스

for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for i in range(v + 1)]
    visited = [False] * (v + 1)
    
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    for i in range(1, v + 1):
        if not visited[i]:
            result = bfs(i, 1)
            if not result:
                break
            
    print('YES' if result else "NO")