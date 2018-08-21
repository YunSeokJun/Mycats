from sys import stdin

N = int(stdin.readline())

check = list()
for x in range(10):
    check.append(10 - x)

for x in range(1,N):
    for x in range(10):
        check[x] = sum(check[x:])

print(check[0]%10007)
