# https://grapestore.tistory.com/m/52

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline


x, y = map(int, input().split()) # x, y에 대한 정보 입력
matrix = []
visited = [[0] * y for _ in range(x)] # visited에 대한 정보 입력
for _ in range(x):
    matrix.append(list(map(int, input().split()))) # matrix에 관련 정보 삽입
    
#동 서 남 북
dx = [0, 0, 1, -1] # 동서남북 리스트 생성
dy = [1, -1, 0, 0] # 동서남북 리스트 생성

# 방문 완료해주는 함수 dfs
def dfs(start_x, start_y): 
    for k in range(4):
        nx = start_x + dx[k] # 동서남북 방향에 따라 행과 열 숫자 변경됨 
        ny = start_y + dy[k] # 동서남북 방향에 따라 행과 열 숫자 변경됨
        
        if nx < 0 or ny < 0 or nx >= x or ny >= y:
            continue
        if matrix[nx][ny] > 0 and visited[nx][ny] == 0: # matrix 상 빙하가 있고, visit 되지 않았으면 방문
            visited[nx][ny] = 1
            dfs(nx, ny) # 방문한 곳을 기준으로 다시 dfs를 돌림

# while 문 시작  
maximum = 0
count = 0
while True:
    cycle_count = 0 # cycle이 존재하는지 확인 (그룹별)
    ice_count = 0 # ice가 존재하는지 확인 (개당)
    visited = [[0] * y for _ in range(x)] 
    
    # 빙하 위치 체크 및 탐색 (이어져 있는 것들끼리)
    for i in range(x):
        for j in range(y):
            if matrix[i][j] > 0:
                ice_count += 1 # ice가 개당 존재하면 +1을 시켜줌
                if visited[i][j] == 0:
                    visited[i][j] = 1
                    dfs(i, j)
                    cycle_count += 1 # 이어져 있는 것들 방문 후 cycle_count + 1
    
    if ice_count < 1:
        break # ice가 하나도 존재하지 않으면 break
    
    # 빙하 크기 내리기
    for i in range(x):
        for j in range(y):
            if matrix[i][j] > 0:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if nx < 0 or ny < 0 or nx >= x or ny >= y:
                        continue
                    if matrix[nx][ny] < 1 and visited[nx][ny] == 0: # 주변이 0이면
                        matrix[i][j] -= 1 # 중심점에서 1만큼 차감
                        
    count += 1 # 크기 내린 후 count + 1
    
    # 빙하가 2조각이면 끝
    if cycle_count > 1:
        print(count - 1)
        exit() # 종료하는 코드

        
print(0)

