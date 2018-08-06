from sys import stdin
import sys
sys.setrecursionlimit(10000)

#DFS
def DFS(graph, start, check):
    if check[start]: return
    check[start] = True # 들어간 자리 = True / 간적 없는곳 = False
    print(start, end = ' ') # 들어간 자리 출력
    for x in graph[start]:
        if check[x]: continue
        DFS(graph, x, check)
#BFS
def BFS(graph, start, check):
    queue = list()
    check[start] = True
    queue.append(start)
    while queue:
        print(queue.pop(), end=' ')
        for x in graph[start]:
            if check[x]: continue
            check[x] = True
            queue = [x] + queue
        if queue : start = queue[-1]
    return

N, M, V = [int(x) for x in stdin.readline().split()]
num_list = [[] for x in range(N+1)]

for x in range(M): #양방항 그래프
    low, col = [int(y) for y in stdin.readline().split()]
    num_list[low].append(col)
    num_list[col].append(low)

for x in range(N): #2차원 list sort
    num_list[x].sort()

check = [False]*(N+1) #정점 확인 list
DFS(num_list, V, check)
print()

check = [False]*(N+1) #정점 확인 list
BFS(num_list, V, check)
