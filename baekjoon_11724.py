from sys import stdin
import sys
sys.setrecursionlimit(10000) # 재귀스택 증가
#DFS
def DFS(start):
    if check[start]: return
    check[start] = True
    for x in graph[start]:
        if check[x]: continue
        DFS(x)

N, M  = [int(x) for x in stdin.readline().split()] # 정점 N / 간선 M
graph = [[] for x in range(N+1)]

for x in range(M):
    u,v = [int(x) for x in stdin.readline().split()]
    graph[u] += [v]
    graph[v] += [u]

check = [False]*(N+1) # 들린곳 확인
check[0] = True
count = 0
for x in range(1, N+1):
    if check[x]: continue
    count += 1
    DFS(x)
print(count)
