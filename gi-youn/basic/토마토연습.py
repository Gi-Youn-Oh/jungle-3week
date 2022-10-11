import sys
from collections import deque
m,n,h = map(int,input().split()) # mn크기, h상자수
graph = []
queue = deque([])
 
for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int,sys.stdin.readline().split())))
        for k in range(m):
            if tmp[j][k]==1: # 익은 토마토가 있다면
                queue.append([i,j,k]) # 큐에 넣기/ # i 칸에 j 행 k열
    graph.append(tmp)
    # 위 아래 왼쪽 오른쪽 앞 뒤 
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 0, 0, -1, 1]
dz = [0, 0, -1, 1, 0, 0]
while(queue):
    z, y, x = queue.popleft() # 동일하게 칸(높이) 행 열 
    
    for i in range(6): # 모든 방향에 대해서 확인 / 
        a = z+dz[i]
        b = y+dy[i]
        c = x+dx[i]
        if 0<=a<h and 0<=b<n and 0<=c<m and graph[a][b][c]==0:
            queue.append([a,b,c])
            graph[a][b][c] = graph[z][y][x]+1
 # 모든 방향을 순회 후에 가능 여부 확인   
day = 0
for i in graph:
    for j in i:
        for k in j:
            if k==0: #graph[i][j][k]
                print(-1)
                exit(0)
        day = max(day,max(j)) # max(j) == graph[i][j][k]
print(day-1)
 