##104ms
from sys import stdin

N = int(stdin.readline())

bread = [0] + list(map(int, stdin.readline().split()))
for x in range(N+1):
     bread[x] = max([bread[x]] + \
                [ bread[y]+bread[x-y] for y in range(x//2,x) ] )

print(bread[-1])

##156ms
from sys import stdin

N = int(stdin.readline())

bread = [0] + list(map(int, stdin.readline().split()))
check = list()
check.append(0)
for x in range(1,N+1):
    if x is 1:
        check.append(bread[x])
        continue
    temp = 0
    for y in range(x//2, x):
        temp = max(check[y]+check[x-y], temp)
    check.append(max(temp,bread[x]))
print(check[-1])
