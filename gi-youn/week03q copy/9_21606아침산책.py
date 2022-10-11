import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def calPaths(graph: list, outinner: list) -> int:
    count = 0
    visited = set()
    # 실외 노드에대한 dfs 로 인접한 노드의 수 계산해서 리턴
    def dfs(out: int) -> int:
        cnt = 0
        for j in graph[out]:
            if outinner[j] == 1:
                cnt += 1
            else:
                if j not in visited:
                    visited.add(j)

                    cnt += dfs(j)
        return cnt

    for i in range(1, N + 1):
        # 각 실내별 인접한 실내 구하기
        if outinner[i] == 1:
            for j in graph[i]:
                if outinner[j] == 1:
                    count += 1
        # 인접한 실외를 한 덩어리로 보고 그 덩어리에 인접한 실내의 수를 구한 뒤 
        # 각 덩어리별로 n*(n-1)의 경우의 수를 계산
        
        # 실외와 인접한 실내의 수 구하기 
        else:
            if i not in visited:
                visited.add(i)
                tmp = dfs(i)   # 실외 노드에 대해서 인접한 실내의 수 찾아서 리턴
                count += tmp * (tmp - 1) # 인접한 실내의 수 tmp tmp*(tmp-1)
 
    return count # 실내 + 실외 더한값
# N = 정점의수
N = int(input())
outinner = list(map(int, list("0"+input().strip())))

graph = [[] for _ in range(N + 1)]

for _ in range(1, N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(calPaths(graph, outinner))

# 이 문제를 O(N)으로 줄일 수 있는 방법은 아래와 같다.

# 어차피 실내 <-> 실내이면서, 중간에 실내를 거치지 않는 길의 개수를 구하는 문제이기 때문에,
# 실외를 하나의 컴포넌트로 생각하여, 그 주변에 인접한 실내의 개수를 dfs로 count해주면 된다. 
# 예를 들어, 주변 인접 실내의 개수가 5개이면, 답에 5*4를 더해주면 된다. 같은 길이어도, 
# 출발점과 도착점이 뒤바뀐 길도 다른 길로 계산하는 문제이기 때문에 2로 나눠줄 필요가 없다.

 
# 또한, 실내 <-> 실내 길 사이에 실외가 하나도 없는 경우는 위 방법으로 count되지 않으므로, 

# 실내이면서 주변 인접 실내인 경우를 count해준다.

# 이렇게 하면 1번부터 N번까지 탐색 O(N), 중간에 DFS가 있긴 하지만, i번에서 DFS로 i~j번까지 탐색한다고 치면, 
# 이후에 i+1~j번까진 이미 DFS로 탐색했기 때문에 추가적으로 탐색할 필요가 없으므로 O(N)의 시간복잡도로 처리할 수 있다.