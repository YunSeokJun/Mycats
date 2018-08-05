#재귀스택 오류
def DFS(graph, stack, visited):
    if not stack: return
    n = stack.pop()
    if n not in visited:
        print(n,end=' ')
        visited.append(n)
        check = list(graph[n] - set(visited))
        check.sort(reverse=True)
        stack += check
    DFS(graph, stack, visited)

def BFS(graph, queue, visited):
    if not queue: return
    n = queue.pop(0)
    if n not in visited:
        print(n, end=' ')
        visited.append(n)
        check = list(graph[n] - set(visited))
        check.sort()
        queue += check
    BFS(graph, queue, visited)

N, M, V = [int(x) for x in input().split()]
num_list = [[0 for x in range(N)] for y in range(N)]
result_list = list()
check_list  = dict()

for x in range(M):
    low, col = [int(x) for x in input().split()]
    num_list[low-1][col-1] = col
    num_list[col-1][low-1] = low

for x in range(N):
    check_list[x+1] = set(num_list[x])
    check_list[x+1].remove(0)

start   = [V]
visit   = []
DFS(check_list, start, visit)

print()

start   = [V]
visit   = []
BFS(check_list, start, visit)
