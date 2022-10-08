# https://backtony.github.io/algorithm/2021-02-18-algorithm-boj-class4-20/

import sys
sys.setrecursionlimit(10 ** 6) # 기본 재귀 깊이 제한은 1000으로 재귀의 깊이를 늘려주는 코드


def post_order(start, end):
    # 역전시 리턴
    if start > end: # 재귀에서 한번 더 들어갔을 때 종료하는 조건
        return
    
    # 루트 노드
    root = pre_order[start]
    idx = start + 1 # pre_order에서 인덱스를 늘려가며 검색해보기 위함
    
    # root보다 커지는 지점을 찾는 과정
    # for 문으로 찾으면 안됨
    while idx <= end:
        if pre_order[idx] > root:
            break # root값 보다 클 때 break 후 아래 왼쪽 서브트리로 넘어감
        idx += 1
        
    # 왼쪽 서브트리
    post_order(start + 1, idx - 1) # root값보다 큰 인덱스 값을 제외하고 왼쪽 서브트리 재귀함수 시작
    
    # 오른쪽 서브트리
    post_order(idx, end) # 왼쪽 서브트리가 끝난 후 오른쪽 서브트리부터 다시 재귀함수 시작

    # 후위 순회이므로 제일 마지막에 찍으면 됨
    print(root)


# 전위 순회를 리스트로 저장해주는 조건
pre_order = [] # [50, 30, 24, 5, 28, 45, 98, 52, 60]
while True:
    try:
        pre_order.append(int(input()))
    # try에서 예외 발생시 break 실행
    except:
        break
    
post_order(0, len(pre_order) - 1)