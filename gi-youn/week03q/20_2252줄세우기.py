import collections
from ipaddress import collapse_addresses
import queue
import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())

graph = [[]for _ in range(n+1)]
indegree = [0] * (n+1) # 모든 노드 진입차수 0 초기화
queue =deque()
answer = []

for i in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b) # 정점 a 에서 b로 이동가능
    indegree[b] += 1 # 진입차수 1증가

for i in range(1, n+1):
    if indegree[i] == 0: # 진입차수가 0 인 노드를 큐에 삽입
        queue.append(i)

while queue:
    tmp = queue.popleft()
    answer.append(tmp)
    for i in graph[tmp]: # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        indegree[i] -= 1
        if indegree[i] == 0: # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            queue.append(i)

print(*answer)