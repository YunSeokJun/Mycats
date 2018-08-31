from sys import stdin
import sys
sys.setrecursionlimit(10000)

def algorithm(day,result):
    t = T[day]
    if day + t is N:
        result = result + P[day]
        print(result)
        return
    elif day + t > N:
        print(result)
        return
    check = [P[x] for x in range(day,day+t) if T[x] <= int(N/2) and T[x] + day <=N]
    temp = max(check)
    day = day + T[day + P[day:day+t].index(temp)]
    result = result + temp
    return algorithm(day,result)

N = int(stdin.readline())
T = list()
P = list()
for x in range(N):
    t, p = map(int, stdin.readline().split())
    T.append(t)
    P.append(p)

day = 0
result = 0
algorithm(day, result)
