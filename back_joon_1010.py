from sys import stdin

T = int(stdin.readline())
rag = list()

for x in range(T):
    rag.append(list(map(int, stdin.readline().split())))

for x in range(len(rag)):
    check = 1
    for y in range(1,rag[x][0]+1):
            check = check*(rag[x][1]-rag[x][0]+y)/y
    print(int(check))
