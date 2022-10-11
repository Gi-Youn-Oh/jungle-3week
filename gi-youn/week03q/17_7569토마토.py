import sys
from collections import deque

input = sys.stdin.readline

# m : 상자 가로 칸 수, n : 상자 세로 칸 수, h : 쌓아올려지는 상자의 수
m, n, h = map(int, input().split())
arr = []
queue = deque()
for i in range(h):
    temp = []
    for j in range(n):
        temp.append(list(map(int, input().split())))
        for z in range(m):
            if temp[j][z] == 1:
                queue.append((i, j, z))
    arr.append(temp)

# 6방향 : 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
directions = [(1, 0, 0), (-1, 0, 0), (0, 0, -1), (0, 0, 1), (0, -1, 0), (0, 1, 0)]

while queue:  # bfs 수행
    hh, nn, mm = queue.popleft()
    for i in range(6):  # 6방향으로 익히기
        hhh = hh + directions[i][0]
        nnn = nn + directions[i][1]
        mmm = mm + directions[i][2]
        if 0 <= hhh < h and 0 <= nnn < n and 0 <= mmm < m and arr[hhh][nnn][mmm] == 0:  # 익힐 수 있는 토마토라면
            arr[hhh][nnn][mmm] = arr[hh][nn][mm] + 1
            queue.append((hhh, nnn, mmm))

result = 0  # 며칠 걸리는지
for i in range(h):
    for j in range(n):
        for z in range(m):
            if arr[i][j][z] == 0:  # 토마토가 모두 익지 못한 상황 발견시
                print(-1)
                exit(0)  # 바로 종료
            else:
                result = max(result, arr[i][j][z])  # 며칠 걸리는지 업데이트

print(result - 1)

