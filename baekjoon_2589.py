from sys import stdin
from collections import deque

def algorithm(row, col, check_temp):
    load = deque()
    load.append([row,col])
    check_temp[row][col] = False
    count = 0
    while load:
        for z in range(len(load)):
            x, y = load.popleft()
            if graph[x+1][y] is 'L' and check_temp[x+1][y]:
                check[x+1][y] = False
                load.append([x+1,y])
            if graph[x-1][y] is 'L' and check_temp[x-1][y]:
                check[x-1][y] = False
                load.append([x-1,y])
            if graph[x][y+1] is 'L' and check_temp[x][y+1]:
                check[x][y+1] = False
                load.append([x,y+1])
            if graph[x][y-1] is 'L' and check_temp[x][y-1]:
                check[x][y-1] = False
                load.append([x,y-1])
        count += 1
    return count

n , k = [int(x) for x in stdin.readline().split()]

graph = [['W'] for x in range(n+2)]
graph[0] += ['W' for x in range(k+1)]

for x in range(1,n+1):
    tmp = stdin.readline()
    for y in range(k): graph[x].append(tmp[y])
    graph[x].append('W')
graph[n+1] += ['W' for x in range(k+1)]

result = 0
for x in range(1, n+1):
    for y in range(1, k+1):
        if graph[x][y] is 'L':
            check = [[True for x in range(k+2)] for x in range(n+2)]
            result = max(algorithm(x,y,check),result)

print(result-1)
