#DFS
def DFS(graph, start, check):
    check[start-1] = True # 들어간 자리 = True / 간적 없는곳 = False
    print(start, end = ' ') # 들어간 자리 출력
    for x in graph[start-1]:
        if not check[x-1]: DFS(graph, x, check)
    return
#BFS
def BFS(graph, start, check):
    queue = list()
    check[start-1] = True
    queue.append(start)
    while queue:
        print(queue.pop(0), end=' ')
        for x in graph[start-1]:
            if not check[x-1]:
                check[x-1] = True
                queue.append(x)
        if queue : start = queue[0]
    return

N, M, V = [int(x) for x in input().split()]
num_list = [[] for x in range(N)]
check_list  = dict()

for x in range(M): #양방항 그래프
    low, col = [int(y) for y in input().split()]
    num_list[low-1].append(col)
    num_list[col-1].append(low)

for x in range(N): #2차원 list sort
    num_list[x].sort()

check = [False]*N #정점 확인 list
DFS(num_list, V, check)
print()
check = [False]*N #정점 확인 list
BFS(num_list, V, check)
