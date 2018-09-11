from sys import stdin

n , k = [int(x) for x in stdin.readline().split()]

line = []
for x in range(n):
    line.append(int(stdin.readline()))

left = 1
right = max(line)
max = 0
while left<=right:
    mid = (left + right) >> 1
    result=0

    for x in line:
        result += x//mid

    if result >= k:
        left = mid + 1
        max = mid
    else: right = mid - 1;

print(max)
