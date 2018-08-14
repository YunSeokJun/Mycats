from sys import stdin

num   = stdin.readline()
times = [int(x) for x in stdin.readline().split()]
times.sort(reverse = True)

check = 0
for x in range(int(num)):
    check = check + (x+1)*times[x]

print(check)
