from collections import deque
from sys import stdin

N, M  = map(int,stdin.readline().split())
check = [[False for m in range(M+2)] for n in range(N+2)]
graph = [[] for x in range(N+2)]
graph[0]  = [0]*(M+2)
graph[-1] = [0]*(M+2)
for x in range(1,N+1):
    graph[x].append(0)
    for y in stdin.readline():
        if y is '\n': continue
        graph[x].append(int(y))
    graph[x].append(0)

result = deque()
result.append([1,1])
check[1][1] = True
num = 0
temp = False
while True:
    num += 1
    for x in range(len(result)):
        miro = result.pop()
        n = miro[0]
        m = miro[1]
        if n is N and m is M:
            temp = True
            break
        if not check[n-1][m] and graph[n-1][m]:
            check[n-1][m] = True
            result.appendleft([n-1,m])
        if not check[n+1][m] and graph[n+1][m]:
            check[n+1][m] = True
            result.appendleft([n+1,m])
        if not check[n][m-1] and graph[n][m-1]:
            check[n][m-1] = True
            result.appendleft([n,m-1])
        if not check[n][m+1] and graph[n][m+1]:
            check[n][m+1] = True
            result.appendleft([n,m+1])
    if temp: break
print(num)
