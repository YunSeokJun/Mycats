from sys import stdin
from collections import deque

M, N  = map(int,stdin.readline().split())
graph = [[] for x in range(N+2)]
check = deque()

graph[0] = [-1]*(M+2)
graph[-1] = [-1]*(M+2)
for x in range(1,N+1):
    graph[x].append(-1)
    for y in stdin.readline().split():
        graph[x].append(int(y))
        if y is '1': check.append([x, len(graph[x])-1]) #  시작점
    graph[x].append(-1)

result = 0 # 총 익을때 까지 걸릴 day

#BFS 사용
while check:
    for x in range(len(check)):
        M = check.pop()
        # 기준점으로 상하좌우 검사
        row = M[0]
        col = M[1]
        if graph[row][col - 1] is 0:
            graph[row][col -1] = 1
            check.appendleft([row, col-1])

        if graph[row][col + 1] is 0:
            graph[row][col + 1] = 1
            check.appendleft([row, col+1])

        if graph[row - 1][col] is 0:
            graph[row - 1][col] = 1
            check.appendleft([row-1, col])

        if graph[row + 1][col] is 0:
            graph[row + 1][col] = 1
            check.appendleft([row+1, col])

    if check: result += 1 # 다음 익을 곳이 있는지 확인하고 day 증가

for x in graph:
    if 0 in x:
        result = -1
        break

print(result)
