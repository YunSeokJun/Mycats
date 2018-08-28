from sys import stdin

T = int(stdin.readline())
rag = list()

for x in range(T):
    N, M = map(int, stdin.readline().split())
    check = 1
    for y in range(1,N+1):
            check = check*(M-N+y)/y
    print(int(check))
