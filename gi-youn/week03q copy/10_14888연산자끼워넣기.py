# 이 문제는 DFS와 백트래킹을 이용했다.
# 문제에서 연산에 사용할 숫자(A1,A2...An)와 연산자의 개수(b1, b2, b3, b4)가 주어진다.
# 연산자는 앞에서 부터 차례대로 더하기, 빼기, 곱하기, 나누기 연산자의 개수를 나타낸다
# 숫자의 순서는 바뀌면 안되며, 연산자의 순서만을 바꿀 수 있다.
# 따라서, 숫자의 순서는 유지한채 연산자를 더하기, 빼기, 곱하기, 나누기를 써가며 식을 바꿔주면 되므로
# 첫 번째 숫자에 첫 연산자를 넣고 DFS를 돌린다음
# 다시 백트래킹을 통해 원래 상태로 돌린 후
# 두 번째 연산자를 넣고 DFS를 돌린다음 다시 백트래킹으로 원래 상태로 돌려
# 모든 경우의 수를 찾아내야 한다.
# 그리고 이 모든 경우의 수 중에 최댓값과 최솟값을 찾아 출력하면 된다.
# 이를 파이썬 코드로 나타내면 다음과 같다.
# 순서대로 if 문 수행 
n = int(input())

data = list(map(int, input().split()))

add, sub, mul, div = map(int, input().split())

max_value = -1e9
min_value = 1e9


def dfs(i, arr):
    global add, sub, mul, div, max_value, min_value

    if i == n:
        max_value = max(max_value, arr)
        min_value = min(min_value, arr)
    else:
        if add > 0:
            add -= 1
            dfs(i+1, arr + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, arr - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, arr * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(arr / data[i]))
            div += 1


dfs(1, data[0])

print(max_value)
print(min_value)
