nm_list = [int(x) for x in input().split()]
check_list = list()
temp_list = [0]*(nm_list[0]-1) #check_list와 길이가 같고 모든 원소가 0인 list
result_list = list()

for x in range(nm_list[0]-1):
    check_list.append(x+2) #check_list에 2부터 N까지 숫자 추가

for x in range(len(check_list)):
    if not temp_list[x]: #원소가 0일때 True
        tmp  = check_list[x]
        temp = int(nm_list[0]/tmp) # N이 tmp의 몇배인지 확인
        for y in range(temp):
            where = check_list.index(tmp*(y+1)) # tmp의 배수 위치 확인
            if not temp_list[where]: #tmp 배수의 위치가 temp_list에서 0일경우 True
                temp_list[where] = 1 #temp_list를 0에서 1로바꿈
                result_list.append(tmp*(y+1)) #tmp배수 result_list에 추가

print(result_list[nm_list[1]-1])
