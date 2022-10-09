# 5639 이진 검색 트리

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
num_list = []

while True:
    try:
        num = int(input())
        num_list.append(num)
    except:
        break

def postorder(first, end):
    if first > end:
        return
    
    div = end+1
    for i in range(first+1, end+1):
        if num_list[first] < num_list[i]:
            div = i
            break

    postorder(first+1, div-1)
    postorder(div, end)
    print(num_list[first])

postorder(0, len(num_list)-1)
    