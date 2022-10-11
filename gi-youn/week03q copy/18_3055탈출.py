import collections
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(input().strip()) for _ in range(n)]
distance = [[0] *m for _ in range(n)]
# 4방향 이동
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

queue = collections.deque()

def bfs(Dx,Dy):
    while queue:
        x,y = queue.popleft()
        if graph[Dx][Dy] == 'S': # 비버의집 위치를 저장후에 bfs를 돌리고 만약 비버의집 위치가 'S' 고슴도치라면 distance값 반환
            return distance[Dx][Dy]
        for i in range(4): # 4방향 이동에 대해서 확인
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m: # 범위를 벗어나면 안됨
                # 고슴도치는 빈칸('.')과 비버의집('D')인 경우만 이동가능하다.
                # 현재위치가 'S'이면 고슴도치가 움직일 차례이다.
                if (graph[nx][ny] == '.' or graph[nx][ny] == 'D') and graph[x][y] == 'S':
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx,ny))
                # 현재위치가 '*'이면 물이 움직일 차례이다.
                # 물은 빈칸('.')과 고슴도치('S')인 경우만 이동가능하다.
                elif (graph[nx][ny] =='.' or graph[nx][ny] =='S') and graph[x][y] == '*':
                    graph[nx][ny] = '*'
                    queue.append((nx,ny))
    return "KAKTUS" # bfs를 모두 돌았는데 'S'가 아니라면 'KAKTUS' 반환하면 된다.

# 고슴도치와 비버의 위치 찾기
for x in range(n):
    for y in range(m):
        if graph[x][y] == 'S': # 고슴도치 위치
            queue.append((x,y))
        elif graph[x][y] == 'D': # 비버
            Dx,Dy = x,y
# 물 위치 찾기
for x in range(n):
    for y in range(m):
        if graph[x][y] == '*':
            queue.append((x,y))

print(bfs(Dx,Dy))

# queue에 고슴도치 위치를 넣어준후에 물에 위치를 넣어줬다 고슴도치가 먼저 이동하고 물이 차도록 만듬

# => 고슴도치가 이동했더라도 물이 이동할 위치라면 고슴도치를 덮어쓰기 때문
# queue에 고슴도치, 물 순서로 들어있으므로 계속 고슴도치 이동후 물 이동하여 graph 값을 변환시켜준다.
# 현재위치가 'S'이면 고슴도치가 움직일 차례이다.
# 고슴도치는 빈칸('.')과 비버의집('D')인 경우만 이동가능하다.

# 현재위치가 '*'이면 물이 움직일 차례이다.
# 물은 빈칸('.')과 고슴도치('S')인 경우만 이동가능하다.

# 비버의집 위치를 저장후에 bfs를 돌리고 만약 비버의집 위치가 'S' 고슴도치라면 distance값 반환
# bfs를 모두 돌았는데 'S'가 아니라면 'KAKTUS' 반환하면 된다.