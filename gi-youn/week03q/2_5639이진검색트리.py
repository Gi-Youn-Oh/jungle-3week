# 후위 순회 / DFS 사용 / 깊이 우선 탐색
# 입력개수 미지수 > while문 사용 / try, except 
# 서브 트리를 찾고, 왼쪽과 오른쪽 서브트리를 재귀적으로 탐색 > 노드 값 출력

# Comment
# 후위순회의 기본에 입각한다.
# 
import sys
sys.setrecursionlimit(10 ** 9) # 재귀 허용 깊이를 수동으로 늘려주는 코드

input = sys.stdin.readline

pre = []

while True:     # 노드의 개수가 10,000개 이하이므로 몇개가 입력될지 모른다. 
    try:
        pre.append(int(input()))
    except:
        break

def post(start, end):
    if start > end:  # 종결조건 이유?  # 
        return
    mid = end + 1 #오른쪽 트리가 존재하지 않을 경우를 대비해 0종결조건 만들어주기.
    for i in range(start + 1, end + 1):
        if pre[i] > pre[start]:    # 오른쪽 함수 왼쪽함수 구분
            mid = i
            break
        # 후위탐색에 의거
    post(start + 1, mid - 1) #왼쪽 트리
    post(mid, end) #오른쪽 트리
    print(pre[start]) #루트 노드

post(0, len(pre) - 1)

# mid를 end + 1로 초기화하는 이유
# 만약 모든 원소가 루트 노드보다 작은 경우 대비
# post(start + 1, mid - 1) : start + 1, end 가 삽입, 즉 루트 노드를 제외한 트리
# post(mid, end) : end + 1, end 가 삽입되어 if start > end: return에 의해 리턴됨 이는 오른쪽 노드가 없음을 의미