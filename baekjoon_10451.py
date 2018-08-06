from sys import stdin

def algorithm(count):
    for x in range(N):
        if check[perm[x]]: continue
        temp = x
        while not check[perm[temp]]:
            check[perm[temp]] = True
            temp = perm[temp] - 1 # 순열의 숫자에 해당하는 각 위치에 어떤 숫자가 있는지 확인
        count += 1
    return count

T = int(stdin.readline()) # TestCase 수
result = list()

for x in range(T):
    N = int(stdin.readline()) # 순열 수
    perm = [int(x) for x in stdin.readline().split()]
    check = [False]*(N+1)
    count = 0
    result.append(algorithm(count))

for x in result:
    print(x)
