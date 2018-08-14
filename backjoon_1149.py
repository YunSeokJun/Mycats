from sys import stdin

N = int(stdin.readline())
R_t = 0
G_t = 0
B_t = 0
for x in range(N):
    RGB = list(map(int, stdin.readline().split()))
    R = min(G_t,B_t) + RGB[0]
    G = min(R_t,B_t) + RGB[1]
    B = min(R_t,G_t) + RGB[2]
    R_t = R
    G_t = G
    B_t = B

result = min(R,min(G,B))

print(result)
