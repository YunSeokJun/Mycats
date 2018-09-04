from sys import stdin

n , k = map(int, stdin.readline().split())

coin= [0 for x in range(k+1)]
coin[0] = 1
for x in range(n):
    input = int(stdin.readline())
    if input <= k:
        m = int(k/input)
        for y in range(input,k+1):
            coin[y] += coin[y - input]

print(coin[-1])
