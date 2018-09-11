from sys import stdin

n , m = map(int, stdin.readline().split())

line = []
right = 0
for x in stdin.readline().split():
    temp = int(x)
    line.append(temp)
    if temp < right: continue
    right = temp

left = 1
max = 0
while left<=right:
    mid = (left + right) // 2
    result=0

    for x in line:
        if x > mid:
            result += x - mid

    if result >= m:
        left = mid + 1
        max = mid
    else: right = mid - 1;

print(max)
