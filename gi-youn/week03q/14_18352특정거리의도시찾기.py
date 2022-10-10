# 이 문제에서 보면 모든 도로의 거리는 '1'이란 조건이 있다.
# 그래프에서 모든 간선(문제에서 도로)의 길이가 동일 할 때는 BFS를 이용하여 최단 거리를 찾을 수 있다.
# 일반적으로 DFS/BFS 알고리즘을 배울때 방문여부를 저장하는 배열을 사용하는데
# 이 문제에서는 방문여부를 저장하는 배열에 거리 정보를 담아서 탐색하면된다.
# distance라는 거리 정보를 답은 배열을 -1로 초기화 한다.
# 탐색시 -1의 값은 아직 방문하지 않은 노드(도시)이다.

# 그리고 문제 설명에서 출발 도시 X에서 X로 가는 최단거리는 항상 0이니
# distance[x] = 0으로 초기화 해준다.
# 그 후 탐색을 하면서 방문하지 않은 다음 도시(next)에 현재 탐색중인(now)의 거리 +1을 넣어 준다.
# 그리고 distance를 조사하여 k와 같은 값이면 출력 k와 같은 값이 하나도 없다면 -1을 출력한다.

import sys
from collections import deque

input = sys.stdin.readline

# N 도시 수, M 도로 수, K 거리 정보 X 출발 도시
N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
  a, b =  map(int, input().split())  
  graph[a].append(b)

distance = [-1] *(N+1)
distance[X] = 0

# BFS 부분
q = deque([X])
while q:
  now = q.popleft()

  for next in graph[now]:
    if distance[next] == -1:
      distance[next] = distance[now]+1
      q.append(next)

# K값이 distance에 있다면 i값출력 없다면 -1 출력
if K in distance:
  for i in range(1, N+1):
    if distance[i] == K:
      print(i)
      check = True
else:
  print(-1)