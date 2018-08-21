from sys import stdin

N = int(stdin.readline())

podo = list()
podo.append(0)
for x in range(N):
    podo.append(int(stdin.readline()))

check = list()
check.append(podo[0])
check.append(podo[1])
if N>1: check.append(podo[1] + podo[2])

result = 0
if N>2:
    for x in range(3,N+1):
        temp = max(podo[x] + podo[x-1] + check[x-3],\
                    podo[x] + check[x-2])
        temp = max(temp, check[x-1])
        check.append(temp)
    result = check[-1]
else:
    result = check[N]

print(result)
