# https://data-flower.tistory.com/72

# dfs 이용

# 수의 개수 입력받기
n = int(input())
# 수열 입력 받기
data = list(map(int, input().split()))
# 연산자 개수 계산
add, sub, mul, div = map(int, input().split())

# 최대값과 최소값 초기화
max_value = -1e9
min_value = 1e9 

# dfs 메서드 정의
def dfs(i, arr):
    global add, sub, mul, div, max_value, min_value 
    # 주어진 수열을 다 받으면 계산
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
            dfs(i+1, int(arr/data[i]))
            div += 1 

# dfs 메서드 호출
dfs(1, data[0])

# 최대, 최소값 출력
print(max_value)
print(min_value)