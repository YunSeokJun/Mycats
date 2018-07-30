nm_list = [int(x) for x in input().split()]
check_list = list()
temp_list = [0]*(nm_list[0]-1)
result_list = list()

for x in range(nm_list[0]-1):
    check_list.append(x+2)

for x in range(len(check_list)):
    if not temp_list[x]:
        tmp  = check_list[x]
        temp = int(nm_list[0]/tmp)
        for y in range(temp):
            where = check_list.index(tmp*(y+1))
            if not temp_list[where]:
                temp_list[where] = 1
                result_list.append(tmp*(y+1))

print(result_list[nm_list[1]-1])
