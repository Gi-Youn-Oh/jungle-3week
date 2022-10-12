import heapq
from sys import maxsize
import sys


input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [maxsize] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b)) # a 출발 , b 도착지, c 비용

start, end = map(int, input().split())


def dijkstra(x):
    q = []
    heapq.heappush(q, (0, x))
    visited[x] = 0

    while q:
        dist, x = heapq.heappop(q)

        if visited[x] < dist:
            continue

        for i in graph[x]:
            cost = dist + i[0]

            if visited[i[1]] > cost:
                heapq.heappush(q, (cost, i[1]))
                visited[i[1]] = cost


dijkstra(start)

print(visited[end])