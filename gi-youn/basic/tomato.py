m, n, h = map(int, input().split())
arr = []

for i in range(h):
    temp = []
    for j in range(n):
        temp.append(list(map(int, input().split())))
print(temp)