n = int(input())
m = int(input())
graph = [[]*n for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
cnt = 0
visited = [0]*(n+1)
def dfs(start):
    global cnt
    visited[start] = 1
    for i in graph[start]:
        if visited[i]==0:
            dfs(i)
            cnt +=1
 
dfs(1)
print(cnt)

# def BFS(virus):
#     global cnt
#     visited[virus] = 1
#     queue = [virus]
#     while queue:
#         for i in network[queue.pop()]:
#             if (visited[i]==0):
#                 visited[i]=1
#                 queue.insert(0, i)
#                 cnt+=1

#DFS(1)

# 둘 다 메모리는 같지만, 시간은 BFS가 108ms, DFS가 104ms로 BFS가 살짝 더 느리게 나왔습니다.
#  하지만, 이론상 BFS가 조금 더 빠릅니다. 이와 같이 나온 이유는 제 코드가 최적화되어 있지 않기 때문이라고 생각합니다. 
#  우선, 리스트로 작성이 되었기 때문에 중복된 값들이 들어갈 수 있습니다. 이는 튜플을 활용해서 시간을 더 줄일 수 있습니다. 
#  다른 사람들의 코드를 참고해보면, 둘 다 실행 시간이 같은 것을 확인할 수 있었습니다. 
#  DFS와 BFS는 상황에 맞게 사용해야 합니다. 대부분의 경우 DFS를 더 선호한다고 합니다. 
#  저도 처음 구현할 때는 DFS부터 작성했던 것 같습니다. 더 많은 문제를 풀어보면서 조금씩 발전해 나가도록 하겠습니다.