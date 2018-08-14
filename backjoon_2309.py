from sys import stdin

dwarfs = list()
for x in range(9):
    dwarf = stdin.readline()
    dwarfs.append(int(dwarf))
dwarfs.sort()

not_dwarfs = sum(dwarfs) - 100
result = False

for x in range(1,9):
    dwarf = dwarfs[9-x]
    if dwarf > not_dwarfs: continue
    check = not_dwarfs - dwarf
    for y in range(1,9-x):
        if check is dwarfs[9-x-y]:
            dwarfs.remove(check)
            result = True
            break
    if result:
        dwarfs.remove(dwarf)
        break

for x in dwarfs:
    print(x)
